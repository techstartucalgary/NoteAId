import { StatusBar } from 'expo-status-bar';
import * as ImagePicker from 'expo-image-picker';
import * as Permissions from 'expo-permissions';
import * as FileSystem from 'expo-file-system';

import React, { useState, useEffect } from 'react';
import { MediaLibrary, Image, Button, ImageBackground, StyleSheet, Text, View, SafeAreaView, ScrollView, TouchableHighlight } from 'react-native';
import NAButton from '../components/NAButton';
import colors from '../config/colors';
function NAHomeScreen({ navigation }) {
//     const [image, setImage] = useState(null);

//   useEffect(() => {
//     (async () => {
//       if (Platform.OS !== 'web') {
//         const { status } = await ImagePicker.requestMediaLibraryPermissionsAsync();
//         if (status !== 'granted') {
//           alert('Sorry, we need camera roll permissions to make this work!');
//         }
//       }
//     })();
//   }, []);

//   const [imageUri, setImageUri] = useState();
//   const [summary, setSummary] = useState();
//   const [summaryDisplay, setSummaryDisplay] = useState("none");

//   const uploadImage = async () => {
//     const formData = new FormData();
//     formData.append('file', {
//       name: 'image.jpg',
//       type: 'image/jpeg',
//       uri: Platform.OS === 'ios' ? imageUri.replace('file://', '') : imageUri,
//     })

//     fetch('http://10.0.0.15:2000//upload', {
//       method: 'POST',
//       // headers: {
//       //   Accept: 'application/json',
//       //   'Content-Type': 'application/json'
//       // },
//       body: formData
//     })
//       .then((res) => res.text())
//       .then((res) => {
//         console.log(res);
//         setSummary(res);
//         setSummaryDisplay('flex')
//       });
//   }

//   const selectImage = async () => {
//     try {
//       const result = await ImagePicker.launchImageLibraryAsync();
//       if (!result.cancelled) {
//         setImageUri(result.uri);
//         uploadImage()
//       }
//     } catch (error) {
//       console.log(error);
//     }
//   }

//   const selectPDF = async () => {
//     try {
//       const result = await FileSystem.requestMediaLibraryPermissionsAsync;
//       if (!result.cancelled) {
//         setImageUri(result.uri);
//       }
//     } catch (error) {
//       console.log(error);
//     }
//   }


  return (
    <ImageBackground style={styles.container} source={require('../assets/bkgBlack.png')}>
      <StatusBar style="light" />

      <SafeAreaView style={styles.topBar}>
        <Text adjustFontSizeToFit={true} style={styles.title}>NoteAid</Text>
        <Text style={styles.subtitle}>Summarise your notes with Ai</Text>
      </SafeAreaView>
      {/* <Image source={{uri: imageUri}} style={{width:200, height: 200}}/> */}

      <View style={styles.buttonArray}>
          <NAButton text="Summarise Photo" color={colors.photo}  onPress={() => navigation.navigate("Photos")} />
          <NAButton text="Summarise PDF" color={colors.pdf} onPress={() => navigation.navigate("PDF")}/>
      </View>

      {/* <View style={{ width: '100%', height: '100%', backgroundColor: '#fff', display: summaryDisplay }}>
        <Text style={{ padding: 30, fontSize: 20 }}>{summary}</Text>
      </View> */}
    </ImageBackground>
  );
}

const styles = StyleSheet.create({
    container: {
      flex: 1,
      backgroundColor: '#E5E5E5',
      //alignItems: 'center',
      //justifyContent: 'center',
    },
    topBar: {
      flex: 1,
      justifyContent: 'flex-start',
      width: '100%',
      alignItems: 'center',   // Along Secondary Axis?
      position: 'absolute'
      //,backgroundColor: 'green'
    },
    title: {
      fontFamily: Platform.OS === "android" ? "Roboto" : "AvenirNext-Bold",
      marginTop: 10, // Redundant
      fontSize: 50,
      paddingTop: 5,
      color: 'white'
    },
    subtitle: {
      fontFamily: Platform.OS === "android" ? "Roboto" : "AvenirNextCondensed-UltraLightItalic",
      fontSize: 18,
      fontWeight: '400',
      color: 'white',
    },
    buttonArray: {
      flex: 1,
      justifyContent: 'flex-end',
      alignContent: 'center'
    },
    defaultText: {
      //backgroundColor:'yellow',
      fontFamily: Platform.OS === "android" ? "Roboto" : "AvenirNext-Bold",
      fontSize: 20,
      color: "white",
    }
  });

export default NAHomeScreen;