import React from "react";
import { View, StyleSheet, ImageBackground, TouchableOpacity } from 'react-native';
import {MaterialCommunityIcons} from "@expo/vector-icons";

import colors from '../config/colors';
import Screen from '../components/Screen'
import AppText from '../components/Text';

function ViewOrSaveScreen({text, color, onPressView, onPressSave, nextScreen, navigation}) {
    onPressSave = () => navigation.navigate("Save/View");

  return (
    <View style={[styles.container, {backgroundColor:color}]}>
        <Screen style={{width: "100%", alignItems:"center"}}>
            <View style={styles.topBar}>
            <AppText style={styles.txt}>{text}</AppText>
            <TouchableOpacity style={styles.rightArrow} onPress={onPressSave} >
            <MaterialCommunityIcons name="content-save-outline" size={30} color={colors.white}/>
            </TouchableOpacity>
            </View>
            <View style={styles.subText}>
            <MaterialCommunityIcons style={{bottom:20,}} name="file-question-outline" size={120} color={colors.white}  />
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
  }, 
  vsButton:{
      width: "40%",
      backgroundColor: "black",
      margin: 10, 
  },
  rightArrow: {
    position: "absolute",
    right: 20,
}
});

export default ViewOrSaveScreen;