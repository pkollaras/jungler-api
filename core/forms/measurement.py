import ast
from itertools import product
from typing import override

from django import forms
from django.conf import settings
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator
from measurement.base import BidimensionalMeasure
from measurement.base import MeasureBase

from core.utils.measurement import get_measurement


class MeasurementWidget(forms.MultiWidget):
    def __init__(self, attrs=None, float_widget=None, unit_choices_widget=None, unit_choices=None, *args, **kwargs):
        self.unit_choices = unit_choices

        if not float_widget:
            float_widget = forms.TextInput(attrs=attrs)

        if not unit_choices_widget:
            unit_choices_widget = forms.Select(attrs=attrs, choices=unit_choices)

        widgets = (float_widget, unit_choices_widget)
        super(MeasurementWidget, self).__init__(widgets, attrs)

    @override
    def decompress(self, value):
        if value:
            if isinstance(value, str):
                try:
                    literal_value = ast.literal_eval(value)
                    magnitude, unit = literal_value
                except (ValueError, SyntaxError):
                    literal_value = value
                    magnitude, unit = [v.strip() for v in literal_value.split(" ")]
                return [float(magnitude), unit]
            elif isinstance(value, MeasureBase):
                choice_units = set([u for u, n in self.unit_choices])
                unit = value.STANDARD_UNIT
                if unit not in choice_units:
                    unit = choice_units.pop()

                magnitude = getattr(value, unit)
                return [magnitude, unit]

        return [None, None]


class MeasurementFormField(forms.MultiValueField):
    def __init__(
        self,
        measurement,
        max_value=None,
        min_value=None,
        unit_choices=None,
        validators=None,
        bidimensional_separator=settings.MEASUREMENT_BIDIMENSIONAL_SEPARATOR,
        *args,
        **kwargs
    ):
        if not issubclass(measurement, (MeasureBase, BidimensionalMeasure)):
            raise ValueError("%s must be a subclass of MeasureBase" % measurement)

        self.measurement = measurement
        if not unit_choices:
            if issubclass(measurement, BidimensionalMeasure):
                assert isinstance(
                    bidimensional_separator, str
                ), "Supplied bidimensional_separator for %s must be of string/unicode type;" " Instead got type %s" % (
                    measurement,
                    str(type(bidimensional_separator)),
                )
                unit_choices = tuple(
                    (
                        (
                            "{0}__{1}".format(primary, reference),
                            "{0}{1}{2}".format(
                                getattr(measurement.PRIMARY_DIMENSION, "LABELS", {}).get(primary, primary),
                                bidimensional_separator,
                                getattr(
                                    measurement.REFERENCE_DIMENSION,
                                    "LABELS",
                                    {},
                                ).get(reference, reference),
                            ),
                        )
                        for primary, reference in product(
                            measurement.PRIMARY_DIMENSION.get_units(),
                            measurement.REFERENCE_DIMENSION.get_units(),
                        )
                    )
                )
            else:
                unit_choices = tuple(
                    ((u, getattr(measurement, "LABELS", {}).get(u, u)) for u in measurement.get_units())
                )

        if validators is None:
            validators = []

        if min_value is not None:
            if not isinstance(min_value, MeasureBase):
                msg = '"min_value" must be a measure, got %s' % type(min_value)
                raise ValueError(msg)
            validators += [MinValueValidator(min_value)]

        if max_value is not None:
            if not isinstance(max_value, MeasureBase):
                msg = '"max_value" must be a measure, got %s' % type(max_value)
                raise ValueError(msg)
            validators += [MaxValueValidator(max_value)]

        float_field = forms.FloatField(*args, **kwargs)
        choice_field = forms.ChoiceField(choices=unit_choices)
        defaults = {
            "widget": MeasurementWidget(
                float_widget=float_field.widget,
                unit_choices_widget=choice_field.widget,
                unit_choices=unit_choices,
            ),
        }
        defaults.update(kwargs)
        fields = (float_field, choice_field)
        super(MeasurementFormField, self).__init__(fields, validators=validators, *args, **defaults)

    def compress(self, data_list):
        if not data_list:
            return None

        value, unit = data_list
        if value in self.empty_values:
            return None

        return get_measurement(self.measurement, value, unit)
