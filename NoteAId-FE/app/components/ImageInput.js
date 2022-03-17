import React, {useEffect} from 'react'
import { Alert, Image, StyleSheet, Text, TouchableWithoutFeedback, View } from 'react-native'
import colors from '../config/colors';
import {MaterialCommunityIcons} from '@expo/vector-icons'
import * as ImagePicker from 'expo-image-picker';

export default function ImageInput({ imageUri, onChangeImage, style, logoColor=colors.medium, logo="camera"}) {
    useEffect(() => {
        requestPermission();
    }, []);
    const requestPermission = async() => {    

        const {granted} = await ImagePicker.requestCameraRollPermissionsAsync();
        if (!granted){
          alert("You need to enable permission to access the library.");
        }
      };


    const handlePress = () => {
        if (!imageUri) selectImage();
        else Alert.alert('Delete', 'Are you sure you want to delete this image?', [
            {text: 'Yes', onPress: () => onChangeImage(null)},
            {text: 'No'}
        ])
    }

    const selectImage = async () => {
        try {
          const result = await ImagePicker.launchImageLibraryAsync({
              mediaTypes: ImagePicker.MediaTypeOptions.Images,
              quality: 0.5,
          });
          if(!result.cancelled){
            onChangeImage(result.uri);
          }
        } catch (error) {
          console.log('Error reading an image', error);
        }
      }
    
    return (
        <TouchableWithoutFeedback onPress={handlePress} >
            <View style={[styles.container, style]}>
                { !imageUri ?
                <MaterialCommunityIcons
                name={logo}
                color={logoColor}
                size={40}
                />:
                <Image source={{uri: imageUri }} style={styles.image}/>
            }
            </View>
        </TouchableWithoutFeedback>
    )
};

const styles = StyleSheet.create({
    container:{
        width: 300,
        height: 480,
        marginBottom: 20,
        backgroundColor: colors.light,
        borderRadius: 15,
        alignItems: 'center',
        justifyContent: 'center',
        overflow: 'hidden',
    },
    image:{
        width: "100%",
        height: "100%",
    }
});