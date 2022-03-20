import React from 'react'
import { createStackNavigator } from '@react-navigation/stack';

import SelectPhotosScreen from '../screens/SelectPhotosScreen';
import colors from '../config/colors';
import ConfirmationScreen from '../screens/ConfirmationScreen';
import SavePhotoScreen from '../screens/SavePhotoScreen';

const Stack = createStackNavigator();

const PhotosNavigator = () => (
    <Stack.Navigator screenOptions={{headerShown:false}}>
        <Stack.Screen name="Select" component={SelectPhotosScreen}/>
        <Stack.Screen name="Save/View" component={SavePhotoScreen}/>
        <Stack.Screen name="Confirm" component={() => <ConfirmationScreen color={colors.photo} text="Your Summary is saved." /> }/>
    </Stack.Navigator>
);

export default PhotosNavigator;