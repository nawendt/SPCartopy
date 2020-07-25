""" SPC Product Colors """

class Outlooks(object):
    categorical = {
        "TSTM": {"ec": "#55BB55", "fc": "#C1E9C1", "label": "Thunder",},
        "MRGL": {"ec": "#005500", "fc": "#66A366", "label": "Marginal",},
        "SLGT": {"ec": "#DDAA00", "fc": "#FFE066", "label": "Slight",},
        "ENH": {"ec": "#FF6600", "fc": "#FFA366", "label": "Enhanced",},
        "MDT": {"ec": "#CC0000", "fc": "#E06666", "label": "Moderate",},
        "HIGH": {"ec": "#CC00CC", "fc": "#EE99EE", "label": "High",},
    }

    tornado = {
        "0.02": {"ec": "#005500", "fc": "#66A366", "label": "2%",},
        "0.05": {"ec": "#70380f", "fc": "#9d4e15", "label": "5%",},
        "0.10": {"ec": "#DDAA00", "fc": "#FFE066", "label": "10%",},
        "0.15": {"ec": "#CC0000", "fc": "#E06666", "label": "15%",},
        "0.30": {"ec": "#CC00CC", "fc": "#EE99EE", "label": "30%",},
        "0.45": {"ec": "#a300cc", "fc": "#d633ff", "label": "45%",},
        "0.60": {"ec": "#2952a3", "fc": "#5c85d6", "label": "60%",},
        "SIGN": {"ec": "#000000", "fc": "#888888", "label": "10% Sig.",},
    }

    wind = {
        "0.05": {"ec": "#70380f", "fc": "#9d4e15", "label": "5%",},
        "0.15": {"ec": "#DDAA00", "fc": "#FFE066", "label": "15%",},
        "0.30": {"ec": "#CC0000", "fc": "#E06666", "label": "30%",},
        "0.45": {"ec": "#CC00CC", "fc": "#EE99EE", "label": "45%",},
        "0.60": {"ec": "#a300cc", "fc": "#d633ff", "label": "60%",},
        "SIGN": {"ec": "#000000", "fc": "#888888", "label": "10% Sig.",},
    }

    hail = {
        "0.05": {"ec": "#70380f", "fc": "#9d4e15", "label": "5%",},
        "0.15": {"ec": "#DDAA00", "fc": "#FFE066", "label": "15%",},
        "0.30": {"ec": "#CC0000", "fc": "#E06666", "label": "30%",},
        "0.45": {"ec": "#CC00CC", "fc": "#EE99EE", "label": "45%",},
        "0.60": {"ec": "#a300cc", "fc": "#d633ff", "label": "60%",},
        "SIGN": {"ec": "#000000", "fc": "#888888", "label": "10% Sig.",},
    }

    any_severe = {
        "0.05": {"ec": "#70380f", "fc": "#9d4e15", "label": "5%",},
        "0.15": {"ec": "#DDAA00", "fc": "#FFE066", "label": "15%",},
        "0.30": {"ec": "#CC0000", "fc": "#E06666", "label": "30%",},
        "0.45": {"ec": "#CC00CC", "fc": "#EE99EE", "label": "45%",},
        "0.60": {"ec": "#a300cc", "fc": "#d633ff", "label": "60%",},
        "SIGN": {"ec": "#000000", "fc": "#888888", "label": "10% Sig.",},
    }

    extended_severe = {
        "0.15": {"ec": "#DDAA00", "fc": "#FFE066", "label": "15%",},
        "0.30": {"ec": "#FF6600", "fc": "#FFA366", "label": "30%",},
    }

    fire_weather_categorical = {
        "ELEV": {"ec": "#e68a00", "fc": "#ffad33", "label": "Elevated",},
        "CRIT": {"ec": "#cc0000", "fc": "#ff3333", "label": "Critical",},
        "EXTM": {"ec": "#CC00CC", "fc": "#EE99EE", "label": "Extreme",},
        "IDRT": {"ec": "#70380f", "fc": "#9d4e15", "label": "Isolated Dry Thunderstorm",},
        "SDRT": {"ec": "#cc0000", "fc": "#ff3333", "label": "Scattered Dry Thunderstorm",},
    }

    extended_fire_weather = {
        "D3": {"ec": "#CC00CC", "fc": "#EE99EE", "label": "Day 3 Critical",},
        "D4": {"ec": "#cc0000", "fc": "#ff3333", "label": "Day 4 Critical",},
        "D5": {"ec": "#a300cc", "fc": "#d633ff", "label": "Day 5 Critical",},
        "D6": {"ec": "#005500", "fc": "#66A366", "label": "Day 6 Critical",},
        "D7": {"ec": "#2952a3", "fc": "#5c85d6", "label": "Day 7 Critical",},
        "D8": {"ec": "#70380f", "fc": "#9d4e15", "label": "Day 8 Critical",},
    }
    