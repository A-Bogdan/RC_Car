# Gesture-Controlled Arduino Car

In the context of the constant evolution of technology and the natural way people use hand gestures to emphasize/integrate their intentions, hand gesture recognition is considered a crucial element in human-computer interaction.

## Table of Contents
- [Project Overview](#project-overview)
  - [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
  - [Assembly and Preparation of the Remote-Controlled Car](#1-assembly-and-preparation-of-the-remote-controlled-car)
  - [Remote Control through a Mobile Application](#2-remote-control-through-a-mobile-application)
  - [Implementation of Commands through Hand Gesture Interpretation](#3-implementation-of-commands-through-hand-gesture-interpretation)
- [Planning and Component Selection](#planning-and-component-selection)
- [Bluetooth RC Controller App](#bluetooth-rc-controller-app)
- [Future Steps](#future-steps)
- [Project Achievements](#project-achievements)

## Project Overview

The project aims to develop a practical and interactive application that, in addition to traditional methods of controlling a remote-controlled car, allows users to maneuver it through gestures captured by the computer's camera.

### Technology Stack

- **Arduino Microcontroller:** A powerful and versatile microcontroller receiving commands via Bluetooth.
- **Computer Camera and Python Programming:** Used for detecting and interpreting user gestures, with a focus on machine learning. Implemented algorithms recognize hand gestures such as "thumbs up," "thumbs down," "peace," and "rock."

## Project Structure

This work is divided into three main chapters:

### 1. Assembly and Preparation of the Remote-Controlled Car

- Detailed presentation of components used.
- Configuration and coordinated connection of components.

### 2. Remote Control through a Mobile Application

- Creation of the program for the Arduino platform.
- Integration with a mobile application, transforming the phone into a practical and portable controller for the remote-controlled car.

### 3. Implementation of Commands through Hand Gesture Interpretation

- Implementation of a real-time machine learning algorithm detecting user hand gestures through the computer camera.

## Planning and Component Selection

Creating a remote-controlled car requires meticulous planning and a logical approach in selecting suitable components. Consideration of a cost-effective budget ensures desired results without compromising quality. Components selected should be reliable, offering long-term performance.

## Bluetooth RC Controller App

The "Bluetooth RC Controller" app, available on the Play Store, is an ideal option for several reasons:

- **Bluetooth Connectivity:** Uses Bluetooth technology for wireless communication between Arduino and mobile devices.
- **User-Friendly Interface:** Designed to be intuitive, enabling even less experienced users to control the Arduino car seamlessly.

## Future Steps

The next phase involves implementing hand gesture recognition and transmitting corresponding commands. This step aims to provide a new perspective on device control, offering a more captivating experience without the need for direct interaction with the mobile application.

## Project Achievements

Throughout the project, we successfully overcame various challenges:

- Identified and resolved assembly and syntax errors to ensure correct car movement.
- Implemented a voltage divider to protect the Bluetooth module (HC-05).
- Chose 18650 batteries for optimal energy storage, low cost, and ease of use.
- Addressed and resolved component quality, particularly with TT motors, through manual shaft processing.
- Opted for Python for a smoother and more elegant Bluetooth connection.

These efforts resulted in a correctly functioning Arduino car controlled by hand gestures, showcasing skills in robotics, electronics, and artificial intelligence.

