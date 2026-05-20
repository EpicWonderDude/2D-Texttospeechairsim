from PIL import Image
img = Image.open("visual_plane_code.py")
def make_background_transparent(input_path, output_path, bg_color=(255, 255, 255), tolerance=30):
    """
    Removes a solid background color from an image and makes it transparent.
    
    :param input_path: Path to the input image
    :param output_path: Path to save the transparent image
    :param bg_color: RGB tuple of the background color to remove
    :param tolerance: Allowed color difference for matching
    """
    try:
        img = Image.open(input_path).convert("RGBA")
        datas = img.getdata()
        new_data = []

        for item in datas:
            if all(abs(item[i] - bg_color[i]) <= tolerance for i in range(3)):
                new_data.append((255, 255, 255, 0))  
            else:
                new_data.append(item)

        img.putdata(new_data)
        img.save(output_path, "PNG")
        print(f"Transparent image saved to {output_path}")

    except FileNotFoundError:
        print("Error: Input file not found.")
    except Exception as e:
        print(f"Error: {e}")

# Example usage
make_background_transparent(
    input_path="input.jpg",
    output_path="output.png",
    bg_color=(255, 255, 255),  # White background
    tolerance=40
)
