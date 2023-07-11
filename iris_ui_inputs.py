"""
Purpose: Provide user interaction options for the iris dataset.

IDs must be unique. They are capitalized in this app for clarity (not typical).
The IDs are case-sensitive and must match the server code exactly.
Preface IDs with the dataset name to avoid naming conflicts.

"""
from shiny import ui


def get_iris_inputs():
    return ui.panel_sidebar(
        ui.h2("Iris Interaction"),
        ui.tags.hr(),
        ui.input_slider(
            "sepal_length",
            "Length of Sepal",
            min=4,
            max=8,
            value=[0.1, 10],
        ),
        ui.tags.hr(),
        ui.tags.section(
            ui.h3("Iris Table"),
            ui.tags.p("Description of each field in the table:"),
            ui.tags.ul(
                ui.tags.li("sepal_length: Length of Sepal"),
                ui.tags.li("sepal_width: Width of Sepal"),
                ui.tags.li("petal_length: Length of Petal"),
                ui.tags.li("petal_width: Width of Petal"),
                ui.tags.li("species: Species"),
                           ),
            ui.output_table("iris_table"),
        ),
        ui.tags.hr(),
        ui.p("🕒 Please be patient. Outputs may take a few seconds to load."),
        ui.tags.hr(),
    )
