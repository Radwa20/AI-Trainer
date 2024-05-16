README

*Check the requirements file first.
Testing the Model

1-Open Test.ipynb.

2-run the test on your video so you should add video's path here:

predict_video(model, 'C:/Users/20109/OneDrive/Desktop/New-Coach2/Test/t2.mp4')

replace # C:/Users/20109/OneDrive/Desktop/New-Coach2/Test/t2.mp4, with your video's path.

3-To open the webcam, replace the path with 0.

#predict_video(model, 0)


Training Your Own Data

1-collect your data set:

*if data are images, use the file: 'PoseImages.py'.

*if data are videos, use the file: 'PoseVideo.py', extract frames using 'ExtractFrames.py'.

2-using Train2.ipynb to train your data.

split your data to train and validation. so it should be like this:

data/
  train/
    bridge/
      img1.jpg
      img2.jpg
      ...
    downward_facing_dog/
      img1.jpg
      img2.jpg
      ...
  val/
    bridge/
      img1.jpg
      img2.jpg
      ...
    downward_facing_dog/
      img1.jpg
      img2.jpg
      ...

replace: 
data_dir = 'C:/Users/20109/OneDrive/Desktop/New-Coach/data'.

with your actual path of your data.


After finishing training and if you want to save your model, replace the placeholder path with the actual path where you want to save it:

torch.save(model.state_dict(), 'C:/Users/20109/OneDrive/Desktop/New-Coach/model.pth')

