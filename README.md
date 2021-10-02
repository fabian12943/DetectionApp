# Detection App

![Detected landmarks of pose and two hands](https://media0.giphy.com/media/d5IpjJCpiTk6D24aJm/giphy.gif?cid=790b76115c292d939a419c054fed8c687d3e38de63665815&rid=giphy.gif)

When finished this application should be able to control various functions of the computer based on hand gestures recognized on the webcam input. For example, controlling the volume, starting a certain program or skipping to the next song.

## Progress
- [x] Read and display webcam input
- [x] Detect pose of most prominent person in frame
- [x] Detect hands in frame
- [ ] Label hands correctly (left hand or right hand)
- [ ] Discard hands that don't belong to most prominent person (for example: hands of people in the background)
- [ ] Define and detect gestures by using the detected landmarks of the hands (for example: 1-4 fingers up, no fingers up, rock'n'roll, peace, thumbs up/down)
- [ ] Implement methods to control various functions of the computer
- [ ] Map gestures to actions to control the computer

### Maybe later
- [ ] Define and detect more complex gestures through machine learning and deep learning with Tensorflow
- [ ] Define and detect sequences of gestures or movement of gestures
- [ ] Create simple GUI to map gestures to actions individually
