/* 3rd Party Imports */
import React from "react";
import 'react-native-gesture-handler';
import { NavigationContainer } from '@react-navigation/native';

/* Screen Imports */
import MainMenuNavigation from "./app/navigation/MainMenuNavigation";

export default function App() {
  return (
    <NavigationContainer>
      <MainMenuNavigation/>
    </NavigationContainer>
  );
}