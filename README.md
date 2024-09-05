# Readme in different languages
[![en](https://img.shields.io/badge/readme-en-blue?style=flat)](https://github.com/Spectra823/MelAdvisor/blob/main/README.md)
[![es](https://img.shields.io/badge/readme-es-yellow?style=flat)](https://github.com/Spectra823/MelAdvisor/blob/main/README.es.md)
[![fr](https://img.shields.io/badge/readme-fr-red?style=flat)](https://github.com/Spectra823/MelAdvisor/blob/main/README.fr.md)

# MelAdvisor
MelAdvisor is an App developed by Carla Marcos Vázquez (aka Spectra823) as a Final Highschool Project for the BIE (Bachillerato de Investigación y Excelencia).
This app's purpose if to classify images of Pigmented Skin Lesions in two groups: melanomas and nevus. In the future it will be possible for the app to classify the image in more types of lesions, but at first we weill only focus on this two until the app is stable enough to improve upon.

The Convolutional Neural Network utilized in this project was also created by Carla for it's exclusive use in this project. 

The app will be available as an APK in this Github for the time being, and might get uploaded to the Google Play Store in the future, time permitting. Making it work on iOS devices is not something I'll be focused on anytime soon, so for now it'll stay as an Android exclusive.

## How it works
MelAvisor utilizes a Convolutional Neural Network (CNN) to classify pigmented lesions in two classes (for now): nevus (benign) and melanoma (malignant). A CNN is a Deep Learning algorithm used in conjuction with a multilayer perceptron. It specializes in image recognition and classification. The algorith asigns weights to the different parts bits of the image, and then compares them to the learnt ones, being able to determine what kind of image model (images used in training) resembles more closely the one given, and then classifies it into that group.

In the future, newer and better functionalities will be added to MelAdvisor. I will leave brief explanations of each one of them here as I go. One of my main concerns with this app is ease of use, so I'll try to keep all simple as concise. 
Nevertheless, if you have any doubts about anything related to MelAdvisor, do not hesitate in contacting me.

## Installation Guide (Android devices only)
1. Download the APK from this link: [https://drive.google.com/file/d/1cS5IhiLOI1d8bVjBEujIV0Dmkq-FfOSD/view?usp=drive_link](https://www.dropbox.com/scl/fi/8kc3y8b19i6zcwmi4a87l/MelAdvisor.apk?rlkey=y8qg6afijucycaszjqfpcehfi&st=e5r6xhwg&dl=0)]([https://drive.google.com/file/d/1cS5IhiLOI1d8bVjBEujIV0Dmkq-FfOSD/view?usp=drivesdk](https://www.dropbox.com/scl/fi/8kc3y8b19i6zcwmi4a87l/MelAdvisor.apk?rlkey=y8qg6afijucycaszjqfpcehfi&st=e5r6xhwg&dl=0))

2. Once downloaded, go to your archives and click on the file. A window should pop up telling you to be careful, as the app is not made by any know source (which means it was not downloaded from an oficial app store like Gogle Play).
It will ask you for permission to install this kind of unknown apps. Click on settings, and then toggle on "Allow from this source".
If it doesnt give you an option to do this automatically, you must go to Settings> Applications> Archives (or whatever app you utilized to store the downloaded file in) and go down until you see "Install unknown apps". Toogle that on.

3. Go back, click on Install. It should take a short time until you see another message saying it was installed succesfully.
Here is a GIF showcasing all the steps:

https://github.com/Spectra823/MelAdvisor/assets/144826015/f46f1a07-15fc-42ab-85b8-7f34b4e95e6d

In case you wish to revoke this permissions, simply go back to that App's Settings and toggle off the "Install unknown apps" option.

## Usage
MelAdvisor is meant to be a simple way to check your pigmented lesions for any melanoma. Early recognition of this kind of malign lesions is crucial, as the chances of survival for this cancer grow slimmer as it develops. 
The simplicity of use of this app allows any user, regardless of their level of knowledge about this issues, to know with a good degree of certainty what their lesions might be. 

What this App is not, and never will be no matter it's level of accuracy, is a replacer for the opinion of a qualified specialist. If you have serious doubts about a lesion, please consider taking your concerns to a dermatologist as soon as possible.
I'm serious. Do not risk your life because taking a picture with my app was easier tha going to a doctor and getting a second, better educated, opinion on the topic.

## Roadmap
### Very probable changes
+Add Local Database: This will allow users to keep track of their lesions' development by taking mutiple pictures in different dates. A file will be created for each new lesion, and in it multiple images of that lesion will be converted into a simple timeline. The user will have to stipulate what lesion the new images belong to after taking it, but there will be a filtering system so it is easier to find the desired lesion. 
This way. they'll be able to know whether or not their lesions are growing, their shape changing... 

I also intend to make it so the file for each lesion can be easily email to medical professionals in a neat PDF showcasing images, time in which they were taken, lesion meassurements...

I wish to make it a local database (stored in the device in which the app is used and not in an external server) for three main reasons:

1. Privacy. I do not want MelAdvisor to keep tabs on what I believe is a very private subject: our users' health. Of coruse, for the sake of making our algorith better, there will be a simple way of sending us information and images so they can be used to train
newer and better models for the App. But this will ALWAYS be optional.

2. Offline use. As all the info is stored in your device, you will we able to access it at any time without needing any kind of Internet connection. I intend for MelAdvisor to be completely Internet-free (except for being able to Google search what a nevus or melanoma is in case you want more infromation, but that's a minor function). This way, more people will be able to use it no matter how good or bad their Internet connection is.

3. Price. As a student, I do not have the monetary means to keep a server up and running (I know there are services that offer servers for like 2 euros a month, but as I said earlier, privacy is a main cocnern for me, and leaving my users info in the hands of an unknown entity is anything but privacy).

The downsides :

1. It will take up space in your device, and ahs the potential to use quite a lot if you take thousands of images.

2. You have to give it access to your device's storage. Yeah, I know, kind of a bummer for us privacy freaks, but I have no other way of doing this (not that I know of, if you have any better ideas please do tell me). I believe this is a better alternative to giving your data to a big corporation that will do God-knows-what with it. I am but a student and can assure you that I have no monetary intent with this App. It is just a passion project that I develop in my free time. 
The good thing is, if you feel like rebuking your trust any day, you can just go into storage and delete all the folders there. Boom, no more data in the database.

+Add a "Wiki" tab: I intent to create a bottom bar with a few more functionalities the first of which will be the Wiki. In it, I intent to briefly explain what is a pigmented lessions, types of lessions that MelAdvisor can classify, advice on what to do after you get each output... This will be an easy way of keeping users informed about anything realted to MelAdvisor in a quick and easy manner. Also, all updates after this one will include a new wiki section so you can know what ahs been added, updated...

### I will do my best, but it's not granted
+Live analysis: being able to analyze and classify videos on the fly, as they are taken. Classifying multiple lesions at once, and being able to create a new folder for each (or add the image to your existing folder) with a simple click over the lesion.
This is quite hard, but not impossible to do. I believe that, with enough time and knowledge, I will be able to do this.

### Very unlikely
+Release for iOS: I'm sorry dear iPhone users, but I do not own a Mac and, frankly, don't think I will be able to afford one just to program this app for you lot. I might try asking a few family members to lend me theirs so I can release a version for you, but I do not know if I would be able to mantain it (cause I cannot borrow their computer everytime I come up with something new or want to apply a quick fix). So, for now, it'll be exclusively an Android App.
Maybe there is a way to install APKs in iOS. I'll try to find another way to get MelAdvisor to you all.
