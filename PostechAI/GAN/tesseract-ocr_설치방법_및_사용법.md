##Tesseract-OCR 설치 방법 및 사용법

이미지에서 문자를 추출하는 기술은 [광학 문자 인식(Optical character recognition; OCR)](https://ko.wikipedia.org/wiki/%EA%B4%91%ED%95%99_%EB%AC%B8%EC%9E%90_%EC%9D%B8%EC%8B%9D)이라는 이름으로 불린다. 이미 많은 *OCR* 기술이 오픈소스로 등록되어 있는데 여기서는 *tesseract-ocr*을 사용해서 이미지에 있는 문자를 추출해 보도록 하자. 



*tesseract*는 구글에서 지원하는 프로젝트이고 인식률이 **OCR** 기술 중 굉장히 높은 편에 속한다고 한다.



우선 *tesseract-ocr*을 다운로드 받고 설치해야 하는데 과정은 아래와 같다. (*wiki*를 참고하면 더욱 자세하게 확인할 수 있다)



필요한 패키지를 설치한다.

```
$ sudo apt-get install autoconf automake libtool
$ sudo apt-get install autoconf-archive
$ sudo apt-get install pkg-config
$ sudo apt-get install libpng12-dev
$ sudo apt-get install libjpeg8-dev
$ sudo apt-get install libtiff5-dev
$ sudo apt-get install zlib1g-dev
```



그리고 추가로 *libleptonica*를 설치한다.

```
$ sudo apt-get install libleptonica-dev
```



이제 본격적으로 *tesseract-ocr*을 사용하기 위해 *GitHub*에서 소스를 다운로드 받아 컴파일 하도록 하자. 

```
$ git clone --depth 1 https://github.com/tesseract-ocr/tesseract.git
$ cd tesseract
$ ./autogen.sh
$ ./configure --enable-debug
$ LDFLAGS="-L/usr/local/lib" CFLAGS="-I/usr/local/include" make
$ sudo make install
$ sudo ldconfig
```



#### 혹시 *configure* 과정에서 버전에 대한 에러가 출력된다면 , 다음을 참고한다.

<hr>

### Tesseract-ocr을 사용하기 위한 leptonica 설치 방법



*tesseract-ocr*을 *configure* 하다보면 아래와 같은 오류가 출력되는 경우가 있다.



> *configure: error: Leptonica 1.74 or higher is required. Try to install libleptonica-dev package.*



무려 *Ubuntu 16.04* 인데 말이다!! 우선 이미지 프로세싱에서 사용되는 *leptonica* 버전을 1.74 혹은 그 이상으로 올려야 한다는 의미인데, *tesseract-ocr*[ ](https://github.com/tesseract-ocr/tesseract/wiki/Compiling)*wiki* 에서 아래와 같이 관련된 내용을 찾아 볼 수 있다.





> but if you are using an oldish version of Linux, the Leptonica version may be too old, so you will need to build from source.
>
> Tesseract versions and the minimum version of Leptonica required:

| Tesseract | Leptonica | Ubuntu                                                       |
| --------- | --------- | ------------------------------------------------------------ |
| 4.00      | 1.74.0    | Must build from source                                       |
| 3.04      | 1.71      | [Ubuntu 16.04](http://packages.ubuntu.com/xenial/libtesseract3) |
| 3.03      | 1.70      | [Ubuntu 14.04](http://packages.ubuntu.com/trusty/libtesseract3) |
| 3.02      | 1.69      | [Ubuntu 12.04](http://packages.ubuntu.com/precise/libtesseract3) |
| 3.01      | 1.67      |                                                              |





내용을 확인 했으면 얌전히 *leptonica*를 다운로드 받아 컴파일 해야 한다. 다운로드는 아래 링크에서 받도록 한다.
<http://www.leptonica.org/download.html>



적절하게 1.74 이상의 버전을 다운로드 받았으면 컴파일을 진행해야 하는데 아래와 같은 과정으로 하면 되겠다.



```
$ ./configure; make; sudo make install
```



*install*시에 *sudo* 권한이 필요할 수 있으며 혹시 컴파일에 이상이 있는 듯 하면 *make check*를 실행하고 에러를 확인해 보면 된다. 이렇게 *leptonica* 설치가 끝났으면 다시 *tesseract-ocr*에 *configure*를 진행해보자. 정상적으로 에러 없이 동작하는 것을 확인할 수 있다.



**donghoon@donghoon:tesseract$** ./configure --enable-debug

checking for g++... g++

checking whether the C++ compiler works... yes

checking for C++ compiler default output file name... a.out

...*중략*

config.status: executing libtool commands



Configuration is done.

You can now build and install tesseract by running:



$ make

$ sudo make install



You can not build training tools because of missing dependency.

Check configure output for details.

#####donghoon@donghoon:tesseract$



<hr>

이제 데이터만 얻으면 모든 과정이 끝났다고 할 수 있다. 여기서 데이터란, 언어를 해석할 수 있도록 도와주는 *datafile* 인데 아래 경로에서 다운로드 받을 수 있다.

<https://github.com/tesseract-ocr/tesseract/wiki/Data-Files>



한글 해석을 위한 *kor*과 *eng* 정도 받으면 되고, 다운로드 받은 파일은 설치 과정에서 별 다른 옵션을 주지 않은 이상 */usr/local/share/tessdata/* 경로에 두면 된다.

현재 기준으로 Updated Data Files for Version 4.00(September 15,2017)

이 가장 최신의 학습된 데이터다.

tessdata_best를 사용하면 비교적 높은 정확도를 유지할 수 있다.



이제 터미널에서 한글 이미지를 테스트 해보도록 한다. 실행 명령은 아래와 같다.

```
$ tesseract test.png outputbase -l kor
```

 확실히 영어에 대한 인식이 높다는 것을 확인할 수 있었다. 영어 이미지는 여러 가지 활용 방안이 있을 수 있겠지만 한글은 그렇지 못하겠다. 이에 대해서는 인식률을 높일 수 있는 방법에 대해서 다시 살펴봐야겠다.



또한 옵션에 보면 *OCR Engine modes*가 여러개 있는데 각각으로 돌려봤을 때 큰 차이를 체감하기 어렵다. traineddata에 는 크게 영향을 받는 것같다. 기존 4.0과 업데이트된 4.0과 차이가 크다.



> *OCR Engine modes:*
>
>   *0    Original Tesseract only.*
>
>   *1    Neural nets LSTM only.*
>
>   *2    Tesseract + LSTM.*
>
>   *3    Default, based on what is available.*



P S. *tesseract-ocr*은 *Apache License*를 따른다.

