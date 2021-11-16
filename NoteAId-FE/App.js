import { StatusBar } from 'expo-status-bar';
import React from 'react';
import { ImageBackground, StyleSheet, Text, View, SafeAreaView, ScrollView, TouchableHighlight } from 'react-native';

export default function App() {
  return (
    <ImageBackground style={styles.container}
    source={require('./assets/bkgBlack.png')}>
      <SafeAreaView style = {styles.topBar}> 
        <Text adjustFontSizeToFit= {true} style={styles.title}>NoteAid</Text>
        <Text style={styles.subtitle}>Summarise your notes with Ai</Text>
      </SafeAreaView>
      <View style={styles.buttonArray}>
        <TouchableHighlight activeOpacity={1} onPress={() => {console.log("Photo Summarised")}}>
          <View style={styles.photoButton}>
            <Text style={styles.defaultText}>Summarise Photo</Text>
          </View> 
        </TouchableHighlight>
        <TouchableHighlight activeOpacity={1} onPress={() => {console.log("PDF Summarised")}}>
          <View style={styles.pdfButton}>
            <Text style={styles.defaultText}>Summarise PDF</Text>
          </View>
        </TouchableHighlight>
      </View>
      
      
      <StatusBar style="auto" />
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
  topBar:{
    flex: 1,
    justifyContent: 'flex-start',
    width: '100%',
    alignItems: 'center',   // Along Secondary Axis?
    position: 'absolute'
    //,backgroundColor: 'green'
  },
  title:{
    fontFamily: "AvenirNext-Bold",
    marginTop: 10, // Redundant
    fontSize: 50,
    paddingTop: 5,
    color: 'white'
  },
  subtitle: {
    fontFamily: "AvenirNextCondensed-UltraLightItalic",
    fontSize: 18,
    fontWeight: '400',
    color: 'white',
  },
  photoButton: {
    //backgroundColor: '#0DA062', // Old colors
    backgroundColor: '#4E7E80',
    width: '100%',
    height: 80,
    alignItems: 'center',
    justifyContent: 'center',
    opacity: 0.86

  },
  pdfButton: {
    //backgroundColor: '#ef476f', // Old Colors
    backgroundColor: '#B86B6B',
    width: '100%',
    height: 80,
    alignItems: 'center',
    justifyContent: 'center',
    opacity: 0.86
  },
  buttonArray:{
    flex: 1,
    justifyContent: 'flex-end',
    alignContent: 'center'
  },
  defaultText:{
    //backgroundColor:'yellow',
    fontFamily: "AvenirNext-Bold",
    fontSize: 20,
    color: "white",
  }
});

// Color Palatte: https://coolors.co/f72585-b5179e-7209b7-560bad-480ca8-3a0ca3-3f37c9-4361ee-4895ef-4cc9f0