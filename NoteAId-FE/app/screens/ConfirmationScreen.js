import React from "react";
import { View, StyleSheet } from 'react-native';
import {MaterialCommunityIcons} from "@expo/vector-icons";

import colors from '../config/colors';
import Screen from '../components/Screen'
import AppText from '../components/Text';

function ConfirmationScreen({text, color, onPress}) {

  return (
    <View style={[styles.container, {backgroundColor:color}]}>
        <Screen style={{width: "100%", alignItems:"center"}}>
            <View style={styles.topBar}>
            <AppText style={styles.txt}>Done!</AppText>
            <MaterialCommunityIcons style={styles.rightArrow} name="chevron-down" size={30} color={colors.white}/>
            </View>
            <View style={styles.subText}>
            <MaterialCommunityIcons style={{bottom:20,}} name="checkbox-marked-circle-outline" size={120} color={colors.white}  />
            <AppText style={[styles.txt,{
                fontSize: 18,
            }]}>{text}</AppText>
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
  rightArrow: {
    position: "absolute",
    right: 20,
}
});

export default ConfirmationScreen;