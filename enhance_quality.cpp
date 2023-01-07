#include <opencv2/opencv.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/dnn_superres.hpp>
#include <iostream>
using namespace std;
using namespace cv;
using namespace dnn;
using namespace dnn_superres;

int main()
{
    cout<<1<<'\n';
    string path_pic = "Textures/de_niro.png";
    cout<<1<<'\n';
    UMat img;
    imread(path_pic).copyTo(img);
    cout<<1<<'\n';
    string path = "EDSR_x4.pb";
    DnnSuperResImpl sr;
    sr.readModel(path);
    sr.setModel("edsr", 4);
    cout<<1<<'\n';
    float start = getTickCount();
    UMat result;
    sr.upsample(img, result);
    cout<<1<<'\n';
    cout << "GPU (with cpp):  " << getTickCount() - start << endl;
    imwrite("enhanced_gpu_cpp.png", result);
}

// #include <iostream>
// #include <opencv2/dnn_superres.hpp>
// #include <opencv2/imgproc.hpp>
// #include <opencv2/highgui.hpp>

// using namespace std;
// using namespace cv;
// using namespace dnn;
// using namespace dnn_superres;

// Mat upscaleImage(Mat img, string modelName, string modelPath, int scale){
//   DnnSuperResImpl sr;
//   sr.readModel(modelPath);
//   sr.setModel(modelName,scale);
//   // Output image
//   Mat outputImage;
//   sr.upsample(img, outputImage);
//   return outputImage;
// }

// int main(int argc, char *argv[])
// {
//   // Read image
//   Mat img = imread("Textures/demq.png");
//   // Region to crop
//   Rect roi;
//   roi.x = 850;
//   roi.y = 0;
//   roi.width = img.size().width - 850;
//   roi.height = 80;
//   img = img(roi);

//   // EDSR (x4)
//   string path = "EDSR_x4.pb";
//   string modelName = "edsr";
//   int scale = 4;
//   Mat result = upscaleImage(img, modelName, path, scale);

//   // Image resized using OpenCV
//   Mat resized;
//   cv::resize(img, resized, cv::Size(), scale, scale);

//   imshow("Original image",img);
//   imshow("SR upscaled",result);
//   imshow("OpenCV upscaled",resized);
//   waitKey(0);
//   destroyAllWindows();

//   return 0;
// }