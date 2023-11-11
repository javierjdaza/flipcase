from PIL import Image


def mm_to_pixels(mm, dpi=600):
    # 1 inch = 25.4 mm
    # pixels = (mm / 25.4) * dpi
    return int((mm / 25.4) * dpi)

def resize_and_crop_image_from_local(image_path1, custom_width_mm=210, custom_height_mm=297, custom_offset_x=0, target_dpi=600, output_path="output_image.jpg"):
    # Open image
    img1 = Image.open(image_path1)

    # Calculate aspect ratio of image 1
    aspect_ratio1 = img1.width / img1.height

    # Calculate dimensions for image 1 to match aspect ratio and fit custom size
    if aspect_ratio1 > 1:
        custom_width = mm_to_pixels(custom_width_mm, target_dpi)
        custom_height = int(custom_width / aspect_ratio1)
    else:
        custom_height = mm_to_pixels(custom_height_mm, target_dpi)
        custom_width = int(custom_height * aspect_ratio1)

    # Resize image 1 to the calculated dimensions
    img1_resized = img1.resize((custom_width, custom_height), Image.LANCZOS)

    # Calculate the offset to center the resized image
    offset_x = int((custom_width_mm - (img1_resized.width / target_dpi) * 25.4) / 2) + mm_to_pixels(custom_offset_x, target_dpi)

    # Crop the image to the specified custom size
    img1_cropped = img1_resized.crop((offset_x, 0, offset_x + mm_to_pixels(custom_width_mm, target_dpi), mm_to_pixels(custom_height_mm, target_dpi)))

    # Create a new image with the specified dimensions
    result_img = Image.new("RGB", (mm_to_pixels(custom_width_mm, target_dpi), mm_to_pixels(custom_height_mm, target_dpi)), (255, 255, 255))

    # Paste the cropped image onto the new image
    result_img.paste(img1_cropped, (0, 0))

    # Set DPI metadata
    result_img.info['dpi'] = (target_dpi, target_dpi)

    # Save the result image
    # result_img.save(output_path, dpi=(target_dpi, target_dpi))

    return result_img

def resize_and_crop_image_from_image(image, custom_width_mm=210, custom_height_mm=297, custom_offset_x=0, target_dpi=600, output_path="output_image.jpg"):
    # Open image
    img1 = image

    # Calculate aspect ratio of image 1
    aspect_ratio1 = img1.width / img1.height

    # Calculate dimensions for image 1 to match aspect ratio and fit custom size
    if aspect_ratio1 > 1:
        custom_width = mm_to_pixels(custom_width_mm, target_dpi)
        custom_height = int(custom_width / aspect_ratio1)
    else:
        custom_height = mm_to_pixels(custom_height_mm, target_dpi)
        custom_width = int(custom_height * aspect_ratio1)

    # Resize image 1 to the calculated dimensions
    img1_resized = img1.resize((custom_width, custom_height), Image.LANCZOS)

    # Calculate the offset to center the resized image
    offset_x = int((custom_width_mm - (img1_resized.width / target_dpi) * 25.4) / 2) + mm_to_pixels(custom_offset_x, target_dpi)

    # Crop the image to the specified custom size
    img1_cropped = img1_resized.crop((offset_x, 0, offset_x + mm_to_pixels(custom_width_mm, target_dpi), mm_to_pixels(custom_height_mm, target_dpi)))

    # Create a new image with the specified dimensions
    result_img = Image.new("RGB", (mm_to_pixels(custom_width_mm, target_dpi), mm_to_pixels(custom_height_mm, target_dpi)), (255, 255, 255))

    # Paste the cropped image onto the new image
    result_img.paste(img1_cropped, (0, 0))

    # Set DPI metadata
    result_img.info['dpi'] = (target_dpi, target_dpi)

    # Save the result image
    # result_img.save(output_path, dpi=(target_dpi, target_dpi))

    return result_img
