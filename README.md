## How to Run The Detector

To run the track limits detection tool, follow these instructions:

1. Start the main application using ```./final_project.sh```
2. Use the GUI to import a video and select the frame you wish to analyze.
3. Use the drawing tools to define the region of interest.
4. Continue to process the image and visualize the track limits.

## Changing Parameters

The only parameters you really need to change are the calls to cv2.Canny() and cv2.HoughLinesP() in the main directory. The Testing Directory should be changed as well in this case. 

That directory just gives quick access to edge detection and output of test images withouth the video import. Follow the naming conventions in the test files or edit them to be more user friendly!

## Contributing

Contributions to the Formula 1 Track Limits Detection package are welcome. Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature/amazing-feature`).
3. Commit your changes (`git commit -m 'Add some amazing feature'`).
4. Push to the branch (`git push origin feature/amazing-feature`).
5. Open a pull request.

## Open Issues

1. Cleaning up test directory for user friendly testing experience.
2. Combining implementation files note that SingleDrawingApp has segfault issue when combining edge detection into same process: needs debugging.
3. Better snapshot experience in GUI
4. Creating preset weather modes or lighting modes that feed cv2.Canny() and cv2.HoughLinesP()

## Note

This was a quick intial implementation hence it's a bit messy but still fun to play around with!

## Contact

Anthony Mensah – admensah@stanford.edu | admensah15@gmail.com

