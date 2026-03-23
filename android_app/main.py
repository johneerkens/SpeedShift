"""Kivy Android-friendly SpeedShift app.

Run locally (desktop preview):
    python3 android_app/main.py
"""

from __future__ import annotations

from kivy.app import App
from kivy.metrics import dp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput

from speedshift_core import SPEED_UNITS_TO_MS, convert_speed


class SpeedShiftLayout(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation="vertical", spacing=dp(12), padding=dp(16), **kwargs)

        self.add_widget(Label(text="SpeedShift", font_size="24sp", size_hint_y=None, height=dp(44)))

        self.value_input = TextInput(
            hint_text="Enter speed value",
            multiline=False,
            input_filter="float",
            size_hint_y=None,
            height=dp(48),
        )
        self.add_widget(self.value_input)

        units = list(SPEED_UNITS_TO_MS.keys())
        self.from_unit = Spinner(
            text="km/h",
            values=units,
            size_hint_y=None,
            height=dp(48),
        )
        self.to_unit = Spinner(
            text="mph",
            values=units,
            size_hint_y=None,
            height=dp(48),
        )
        self.add_widget(self.from_unit)
        self.add_widget(self.to_unit)

        convert_button = Button(text="Convert", size_hint_y=None, height=dp(52))
        convert_button.bind(on_press=self.on_convert)
        self.add_widget(convert_button)

        clear_button = Button(text="Clear", size_hint_y=None, height=dp(52))
        clear_button.bind(on_press=self.on_clear)
        self.add_widget(clear_button)

        self.result_label = Label(text="", font_size="20sp")
        self.add_widget(self.result_label)

    def on_convert(self, _instance):
        raw_value = self.value_input.text.strip()
        if not raw_value:
            self.result_label.text = "Please enter a value"
            return

        try:
            value = float(raw_value)
            result = convert_speed(value, self.from_unit.text, self.to_unit.text)
        except ValueError:
            self.result_label.text = "Invalid number"
            return
        except KeyError:
            self.result_label.text = "Unsupported unit"
            return

        self.result_label.text = f"{result:.4f} {self.to_unit.text}"

    def on_clear(self, _instance):
        self.value_input.text = ""
        self.result_label.text = ""


class SpeedShiftApp(App):
    def build(self):
        self.title = "SpeedShift"
        return SpeedShiftLayout()


if __name__ == "__main__":
    SpeedShiftApp().run()
