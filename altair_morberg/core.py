# AUTOGENERATED! DO NOT EDIT! File to edit: 00_core.ipynb (unless otherwise specified).

__all__ = ['theme']

# Cell
def theme():
    """Niklas Morberg's personal theme for Altair"""
    return {
        "config": {
            "axis": {
                "labelFontSize": 12,
                "labelColor": "#666",
                "titleFontSize": 14,
                "titleFontWeight": "normal",
                "titleColor": "#666",
            },
            "axisX": {"grid": False, "gridWidth": 0.4},
            "axisY": {"gridDash": [3], "gridWidth": 0.4, "offset": 10},
            "legend": {
                "titleFontSize": 14,
                "titleFontWeight": "normal",
                "titleColor": "#666",
                "labelColor": "#666",
                "labelFontSize": 13,
            },
            "font": "Avenir Next, sans-serif",
            "header": {
                "labelFontSize": 14,
                "labelColor": "#666",
                "titleFontSize": 16,
                "titleFontWeight": "normal",
                "titleColor": "#666",
            },
            "headerRow": {"labelFontSize": 14, "labelColor": "#666"},
            "title": {
                "anchor": "start",
                "frame": "group",
                "offset": 10,
                "fontSize": 24,
                "font": "Avenir Next Demi Bold, Avenir Next, sans-serif",
            },
            "view": {"strokeWidth": 0, "continuousWidth": 600, "continuousHeight": 400},
        }
    }