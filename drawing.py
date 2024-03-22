import cv2
import numpy as np
import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk, ImageDraw, ImageFilter

class SingleShapeDrawingApp:
    def __init__(self, root, filename):
        self.root = root
        self.filename = filename
        # Load the background image with PIL using the filename parameter
        self.background_image = Image.open(filename)
        self.background_photo = ImageTk.PhotoImage(self.background_image)
        
        self.canvas = tk.Canvas(root, width=self.background_photo.width(), height=self.background_photo.height())
        self.canvas.pack()
        
        # Set the background image
        self.canvas.create_image(0, 0, image=self.background_photo, anchor="nw")
        self.setup()

        # Initialize a mask where everything is filled (opaque) by default
        self.mask = Image.new("RGBA", self.background_image.size, (0, 0, 0, 255))
        self.mask_draw = ImageDraw.Draw(self.mask)  # Create a drawing context for the mask

        # Create a button to finalize the image
        self.finalize_button = tk.Button(root, text="Finalize Image", command=self.finalize_image)
        self.finalize_button.pack()

        self.done_button = tk.Button(root, text="Done", command=self.done)
        self.done_button.pack()

        self.root.bind('<f>', lambda event: self.finalize_image())
        self.root.bind('<d>', lambda event: self.done())

    def setup(self):
        self.points = []
        self.temp_shape_id = None
        self.canvas.bind('<B1-Motion>', self.record_point)
        self.canvas.bind('<ButtonRelease-1>', self.draw_shape_and_finalize)

    def record_point(self, event):
        self.points.append((event.x, event.y))
        self.update_temporary_shape()

    def draw_shape_and_finalize(self, event):
        if len(self.points) > 2:
            # Draw the final shape on the canvas
            self.canvas.create_polygon(self.points, outline='red', fill='', width=4)
            # Cut out the shape on the mask (making inside of the shape transparent)
            self.mask_draw.polygon(self.points, fill=(0, 0, 0, 0))
        if self.temp_shape_id is not None:
            self.canvas.delete(self.temp_shape_id)
        self.points = []
        self.temp_shape_id = None

    def update_temporary_shape(self):
        if len(self.points) > 1:
            if self.temp_shape_id is not None:
                self.canvas.delete(self.temp_shape_id)
            self.temp_shape_id = self.canvas.create_polygon(self.points, outline='blue', fill='', dash=(3, 5), width=4)

    def finalize_image(self):
        # Blend the mask with the original background image
        mask_blurred = self.mask.filter(ImageFilter.GaussianBlur(radius=5))
        final_image = Image.alpha_composite(self.background_image.convert("RGBA"), self.mask)
        
        # Save the final image to a file
        save_path = "masked_image.png"  # You can change the file name and path as needed
        final_image.save(save_path, "PNG")

        # Update the canvas with the final image
        final_photo = ImageTk.PhotoImage(final_image)
        self.canvas.delete(self.background_image)
        self.canvas.create_image(0, 0, image=final_photo, anchor="nw")
        self.background_photo = final_photo  # Update the reference to keep the image displayed
        
    def done(self):
        self.root.destroy()

    def lines():
        # Read image
        image = cv2.imread("masked_image.png", cv2.IMREAD_GRAYSCALE)

        lines = cv2.HoughLinesP(
            image, 
            1,  
            np.pi / 180,  
            threshold=150,  
            minLineLength=25, 
            maxLineGap=10  
        )

        # Avoid the lines outside of the desired area
        width = image.shape[1]
        lines_list = []

        background_image = cv2.imread("snapshot.jpg")

        # Check if any lines are detected
        if lines is not None:
            for points in lines:
                x1, y1, x2, y2 = points[0]
                # Draw the line on the background image
                cv2.line(background_image, (x1, y1), (x2, y2), (255, 0, 0), 3)

        # Display the result with lines drawn on the background image
        cv2.imshow('Final Lines (Press any key to continue)', background_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

        # Write the result
        cv2.imwrite('output_with_lines.jpg', background_image)

root = tk.Tk()
app = SingleShapeDrawingApp(root, 'edges.jpg')
root.mainloop()
SingleShapeDrawingApp.lines()
