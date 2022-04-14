import React from 'react'
import { createStackNavigator } from '@react-navigation/stack';

import SelectPDFScreen from '../screens/SelectPDFScreen';
import colors from '../config/colors';
import ConfirmationScreen from '../screens/ConfirmationScreen';
import SavePDFScreen from '../screens/SavePDFScreen';


const Stack = createStackNavigator();

const PDFNavigator = () => (
    <Stack.Navigator screenOptions={{ headerShown: false }}>
        <Stack.Screen name="Select" component={SelectPDFScreen} />
        <Stack.Screen name="Save/View" component={SavePDFScreen} />
        <Stack.Screen name="Confirm" component={ConfirmationScreen} />
        {/* component={() => <ConfirmationScreen color={colors.pdf} text="Your Summary is saved." /> } */}
    </Stack.Navigator>
);

export default PDFNavigator;