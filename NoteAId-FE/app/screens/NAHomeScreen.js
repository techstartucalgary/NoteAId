import { StatusBar } from 'expo-status-bar';
import * as ImagePicker from 'expo-image-picker';
import * as Permissions from 'expo-permissions';
import * as FileSystem from 'expo-file-system';

import React, { useState, useEffect } from 'react';
import { MediaLibrary, Image, Button, ImageBackground, StyleSheet, Text, View, SafeAreaView, ScrollView, TouchableHighlight } from 'react-native';
import NAButton from '../components/NAButton';
import colors from '../config/colors';
function NAHomeScreen({ navigation }) {

  return (
    <View style={styles.container}>
      <StatusBar style="light" />

      <Image style={{ height: "100%", width: "100%", position: "absolute", "left": 0, "top": 0 }} source={require('../assets/app_background.gif')} />

      <SafeAreaView style={styles.topBar}>
        <Text adjustFontSizeToFit={true} style={styles.title}>NoteAid</Text>
        <Text style={styles.subtitle}>Summarize your notes using AI</Text>
      </SafeAreaView>

      <View style={styles.buttonArray}>
        <NAButton text="Summarize Photo" color={colors.photo} onPress={() => navigation.navigate("Photos")} />
        <NAButton text="Summarize PDF" color={colors.pdf} onPress={() => navigation.navigate("PDF")} />
      </View>

    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#E5E5E5',
    height: "100%",
    width: "100%",
    position: "relative"
    //alignItems: 'center',
    //justifyContent: 'center',
  },
  topBar: {
    flex: 1,
    justifyContent: 'flex-start',
    width: '100%',
    alignItems: 'center',   // Along Secondary Axis?
    position: 'absolute',
    marginTop: Platform.OS === "android" ? 50 : 0
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