import React, { useEffect, useState } from "react";
import { View, StyleSheet, ImageBackground, TouchableOpacity } from 'react-native';
import {MaterialCommunityIcons} from "@expo/vector-icons";

import colors from '../config/colors';
import Screen from '../components/Screen'
import AppText from '../components/Text';
import ImageInputList from '../components/ImageInputList';

function LoadingScreen({text, color}) {
    const[images, setImages] = useState([]);

    const handleAdd = uri => {
        setImages([...images, uri]);
    }

    const handleRemove = uri => {
        setImages(images.filter(imageUri => imageUri !== uri));
    }

  return (
    <View style={[styles.container, {backgroundColor:color}]}>
        <Screen style={{width: "100%", alignItems:"center"}}>
            <View style={styles.topBar}>
            <AppText style={styles.txt}>{text}</AppText>
            </View>
            <View style={styles.subText}>
            <MaterialCommunityIcons style={{bottom:20,}} name="progress-upload" size={120} color={colors.white}  />
            <AppText style={[styles.txt,{
                fontSize: 18,
            }]}>Sit tight, our ai is working hard.</AppText>
            </View>
        </Screen>
    </View> 
  );
}

const styles = StyleSheet.create({
  container: {
      backgroundColor: colors.pdf,
      flex: 1,
      alignItems: 'center',
  },
  txt:{
      marginTop: 10,
      marginBottom: 20,
      color: colors.white,
      fontSize: 20,
      alignSelf: "center",
  },
  topBar:{
      flexDirection: "row",
      width: "100%",
      justifyContent: "center",
  },
  subText:{
      flex: 1,
      justifyContent: "center",
      alignItems: "center",
  }
});

export default LoadingScreen;