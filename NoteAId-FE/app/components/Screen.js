import React from "react";
import Constants from "expo-constants";
import { StyleSheet, View } from "react-native";

function Screen({ children, style }) {
  return (
    <View style={[styles.screen, style]}>
      <View style={[styles.view, style]}>{children}</View>
    </View>
  );
}

const styles = StyleSheet.create({
  screen: {
    marginTop: Constants.statusBarHeight,
    flex: 1,
  },
  view: {
    flex: 1,
  },
});

export default Screen;
