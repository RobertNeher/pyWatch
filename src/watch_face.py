import flet as ft
import flet.canvas as cv

def watch_face(radius: float):
    stroke_paint = ft.Paint(color=ft.colors.BLACK26, stroke_width=5, style=ft.PaintingStyle.STROKE)
    fill_paint = ft.Paint(color=ft.colors.BLACK12, style=ft.PaintingStyle.FILL)
    return cv.Canvas(
        [
            cv.Circle(radius, radius, radius, fill_paint),
            cv.Circle(radius, radius, radius * 0.97, stroke_paint),
            cv.Circle(radius, radius, radius * 0.05, fill_paint)
        ],
        width=float("inf"),
        expand=True,
    )
