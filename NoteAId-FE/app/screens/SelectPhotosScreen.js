import React, { useEffect, useState } from "react";
import { View, StyleSheet, ImageBackground, TouchableOpacity } from 'react-native';
import {MaterialCommunityIcons} from "@expo/vector-icons";

import colors from '../config/colors';
import Screen from '../components/Screen'
import AppText from '../components/Text';
import ImageInputList from '../components/ImageInputList';

function SelectPhotosScreen({navigation, onPress}) {
    onPress = () => navigation.navigate("Save/View");

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
            <AppText style={styles.txt}>Select Photos</AppText>
            <TouchableOpacity style={styles.rightArrow} onPress={onPress} >
            <MaterialCommunityIcons name="arrow-right" size={30} color={colors.white}/>
            </TouchableOpacity>
            </View>

            <View style={styles.imgContainer}>
            <ImageInputList
            addLogo="camera"
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
        //width: "100%",
        
    },
  container: {
      backgroundColor: colors.photo,
      flex: 1,
      alignItems: 'center',
      width: "100%",
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
      //alignItems: "center",
      width: "100%",
      justifyContent: "center",
      //backgroundColor: "red"
      //width: 300,
  },
  rightArrow: {
      position: "absolute",
      right: 20,
  }
});

export default SelectPhotosScreen;