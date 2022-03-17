import React from 'react'
import { createStackNavigator } from '@react-navigation/stack';

import NAHomeScreen from '../screens/NAHomeScreen';
import SelectPDFScreen from '../screens/SelectPDFScreen';
import SelectPhotosScreen from '../screens/SelectPhotosScreen';
import PhotosNavigator from './PhotosNavigator';
import PDFNavigator from './PDFNavigator';

const Stack = createStackNavigator();

const MainMenuNavagation = () => (
    <Stack.Navigator screenOptions={{headerShown:false}} mode="modal">
        <Stack.Screen name="Welcome" component={NAHomeScreen}/>
        <Stack.Screen name="PDF" component={PDFNavigator} />
        <Stack.Screen name="Photos" component={PhotosNavigator}/>
    </Stack.Navigator>
);

export default MainMenuNavagation;