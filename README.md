# Train Predict Landmarks by MCAM
 Train Predict Landmarks by Multi-context attention model


based on the code: <br>
https://github.com/wbenbihi/hourglasstensorlfow

# prepation

- generate the text files contains the information of the landmarks for each image in the train folder.  <br>
- set the annotaion file path and other configs such as epochs, stack levels and etc. in config file.<br>

Following image shows an example of folders, annotation text file and config file for training. more information is availble at the original repositort mentioned above. <br>

![Alt text](preparation.png?raw=true "Title")


# train

> python train_launcher.py <br>

for reading the logs:  <br>
>        tensorboard --logdir=./Logs/ <br>
>        tensorboard --logdir=./Logs-test/

# predict
use following shell and asssinging the input directoty, path of the trained model and output directory <br>
> python pr_predict.py --input_dir  ./temp_test_png --checkpoint  ./hg_refined_200  --output_dir ./Results/ <br>

images and text files of the prediction are available at the Results folder:

![Alt text](result.png?raw=true "Title")
