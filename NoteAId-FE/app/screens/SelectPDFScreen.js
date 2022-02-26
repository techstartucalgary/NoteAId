import React, { useState } from "react";
import { View, StyleSheet, TouchableOpacity } from 'react-native';
import {MaterialCommunityIcons} from "@expo/vector-icons";

import colors from '../config/colors';
import Screen from '../components/Screen'
import AppText from '../components/Text';
import ImageInputList from '../components/ImageInputList';

function SelectPDFScreen({onPress, navigation}) {
    onPress= () => navigation.navigate("Save/View");

    const[images, setImages] = useState([]);

    const handleAdd = uri => {
        setImages([...images, uri]);
    }

    const handleRemove = uri => {
        setImages(images.filter(imageUri => imageUri !== uri));
    }

  return (
    <View style={styles.container}>
        <Screen style={{width: "100%", alignItems:"center"}}>
            <View style={styles.topBar}>
            <AppText style={styles.txt}>Select PDF</AppText>
            <TouchableOpacity style={styles.rightArrow} onPress={onPress} >
            <MaterialCommunityIcons name="arrow-right" size={30} color={colors.white}/>
            </TouchableOpacity>
            </View>

            <View style={styles.imgContainer}>
            <ImageInputList
            logoBackgroundColor={colors.pdf}
            addLogo="text-box-plus-outline"
            style={styles.images}
            imageUris={images}
            onAddImage={handleAdd}
            onRemoveImage={handleRemove}
            />
            </View>
        </Screen>
    </View> 
  );
}

const styles = StyleSheet.create({
    imgContainer:{
        
    },
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
  rightArrow: {
      position: "absolute",
      right: 20,
  }
});

export default SelectPDFScreen;