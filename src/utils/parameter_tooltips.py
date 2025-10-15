"""
Parameter Tooltips and Descriptions
English descriptions for V4L2 camera parameters
"""

# Parameter descriptions for tooltips
PARAMETER_TOOLTIPS = {
    # Basic Image Controls
    "brightness": "Brightness: Adjusts the overall lightness/darkness of the image. Higher values make the image brighter.",
    "contrast": "Contrast: Controls the difference between light and dark areas. Higher values increase contrast.",
    "saturation": "Saturation: Controls color intensity. Higher values make colors more vivid, lower values make them more muted.",
    "hue": "Hue: Adjusts the color tint/tone of the image. Changes the overall color balance.",
    "gamma": "Gamma: Controls the relationship between input and output luminance. Affects mid-tone brightness.",
    "sharpness": "Sharpness: Controls edge enhancement. Higher values make edges more defined but may introduce artifacts.",
    
    # White Balance
    "white_balance_temperature": "White Balance Temperature: Color temperature in Kelvin. Lower values are warmer (reddish), higher values are cooler (blueish).",
    "white_balance_temperature_auto": "Auto White Balance: Automatically adjusts white balance based on lighting conditions.",
    "do_white_balance": "Do White Balance: Trigger automatic white balance calibration once.",
    
    # Exposure Controls
    "exposure_auto": "Auto Exposure: Controls automatic exposure adjustment. 0=Manual, 1=Auto, 2=Shutter Priority, 3=Aperture Priority.",
    "exposure_absolute": "Exposure Time: Manual exposure time in 100µs units. Lower values = shorter exposure (darker), higher = longer (brighter).",
    "exposure_auto_priority": "Auto Exposure Priority: Prioritizes correct exposure over frame rate when enabled.",
    
    # Gain Controls
    "gain": "Gain: Amplifies the signal from the sensor. Higher values brighten the image but increase noise.",
    "gain_automatic": "Auto Gain: Automatically adjusts gain based on lighting conditions.",
    
    # Power Line Frequency
    "power_line_frequency": "Power Line Frequency: Reduces flicker from artificial lighting. Set to your AC frequency (50Hz/60Hz).",
    
    # Backlight Compensation
    "backlight_compensation": "Backlight Compensation: Corrects for strong backlighting that makes subjects appear dark.",
    
    # Focus Controls
    "focus_absolute": "Focus Position: Manual focus position. Higher values typically focus further away.",
    "focus_auto": "Auto Focus: Enables automatic focus adjustment.",
    "focus_relative": "Focus Relative: Adjusts focus relative to current position. Positive = focus further, negative = closer.",
    
    # Zoom Controls
    "zoom_absolute": "Zoom Level: Absolute zoom level. Higher values zoom in more.",
    "zoom_relative": "Zoom Relative: Adjusts zoom relative to current level. Positive = zoom in, negative = zoom out.",
    "zoom_continuous": "Continuous Zoom: Enables smooth continuous zoom operation.",
    
    # Pan/Tilt Controls
    "pan_absolute": "Pan Position: Horizontal camera position in degrees. Negative = left, positive = right.",
    "tilt_absolute": "Tilt Position: Vertical camera position in degrees. Negative = down, positive = up.",
    "pan_relative": "Pan Relative: Adjusts pan relative to current position.",
    "tilt_relative": "Tilt Relative: Adjusts tilt relative to current position.",
    "pan_reset": "Pan Reset: Resets pan position to center (0 degrees).",
    "tilt_reset": "Tilt Reset: Resets tilt position to center (0 degrees).",
    
    # Color Controls
    "red_balance": "Red Balance: Adjusts red color component intensity.",
    "blue_balance": "Blue Balance: Adjusts blue color component intensity.",
    "chroma_gain": "Chroma Gain: Controls color saturation in YUV color space.",
    
    # Noise Reduction
    "noise_reduction": "Noise Reduction: Reduces image noise, especially in low light. May soften details.",
    
    # Image Effects
    "color_effects": "Color Effects: Apply special color effects (None, Black&White, Sepia, etc.).",
    "rotate": "Rotate: Rotates the image by specified degrees (0, 90, 180, 270).",
    
    # Advanced Controls
    "auto_exposure_bias": "Exposure Bias: Biases auto exposure towards brighter/darker results.",
    "iso_sensitivity": "ISO Sensitivity: Light sensitivity setting. Higher values brighten image but increase noise.",
    "iso_sensitivity_auto": "Auto ISO: Automatically adjusts ISO based on lighting conditions.",
    
    # Video Format Controls
    "horizontal_flip": "Horizontal Flip: Mirrors the image horizontally (left-right).",
    "vertical_flip": "Vertical Flip: Mirrors the image vertically (top-bottom).",
    
    # Band-stop Filter
    "band_stop_filter": "Band Stop Filter: Filters out specific frequency bands to reduce interference.",
    
    # Scene Mode
    "scene_mode": "Scene Mode: Optimizes camera settings for specific scenarios (Portrait, Landscape, Sports, etc.).",
    
    # Link Frequency
    "link_freq": "Link Frequency: Communication frequency between sensor and processor.",
    
    # Pixel Rate
    "pixel_rate": "Pixel Rate: Rate at which pixels are processed/transmitted.",
}

def get_parameter_tooltip(parameter_name: str) -> str:
    """
    Get tooltip text for a parameter
    
    Args:
        parameter_name: Name of the V4L2 parameter
        
    Returns:
        Tooltip text or generic description if not found
    """
    return PARAMETER_TOOLTIPS.get(
        parameter_name, 
        f"{parameter_name.replace('_', ' ').title()}: Camera parameter control"
    )

def get_all_tooltips() -> dict:
    """Get all available parameter tooltips"""
    return PARAMETER_TOOLTIPS.copy()