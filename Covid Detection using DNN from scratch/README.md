# Covid19-Detection-using-DNN

The model behaved somehow badly with only **64% accuracy** because of more positive data as compare to negative data. Also because of   small dataset of only 200+ images
- First converted the images into 64X64 pixels and used there rgb values to create the features of array
- Code is well explained in the jupyter notebook with the headings and comments
- Create your dataset yourself with the following command which converts the image into its path stored in file
 ```bash
  dir /b/s/w *.jpg > "filename.csv"
```
- Then create the header of whatever columns you want to add

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
