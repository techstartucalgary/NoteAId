import React from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity } from 'react-native';
const App = () => {
  return (
    <View style={styles.container}>
      <Image source={require('./assets/bkgBlack.png')} style={styles.backgroundImage}/>
      <View style={styles.footer}>
        <View style={styles.upper}>
          <View style={styles.left}>
            <Text style={styles.title}>Done!</Text>
          </View>
          <View style={styles.right}>
            <TouchableOpacity onPress = {() => {console.log("closed")}}>
              <Image source={require('./assets/close.png')} style={styles.close}/>
            </TouchableOpacity>
          </View>
        </View>
        <View style = {styles.checkIcon}>
          <Image source={require('./assets/check.png')} style={styles.icon}/>
        </View>

        <View style = {styles.buttons}>
          <View style = {styles.saveButton}> 
            <TouchableOpacity onPress = {() => {console.log("saved")}}>
                <Text style = {styles.saveText}> Save </Text>
            </TouchableOpacity>
          </View>
          <View styles = {styles.saveButton}>
            <TouchableOpacity onPress = {() => {console.log("view")}}>
                <Text style = {styles.saveText}> View </Text>
            </TouchableOpacity>
          </View>
        </View>
      </View>
    </View>
  );
}

export default App;

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#262431',
  },
  backgroundImage: {
    flex: 1,
    justifyContent: 'center'
  },
  footer: {
    flex: 9,
    backgroundColor: '#4E7E80',
    borderTopLeftRadius: 30,
    borderTopRightRadius: 30,
    alignItems: 'center'
  },
  upper:{
    flex: 2,
    flexDirection: 'row'
  },
  left:{
    flex: 2,
    flexDirection: 'column',
    alignItems: 'flex-end'
  },
  title: {
    fontFamily: 'AvenirNext-Regular',
    fontSize: 40,
    marginTop: 30,
    color: 'white'
  },
  right:{
    flex: 1,
    flexDirection: 'column',
    alignItems: 'flex-end'
  },
  close: {
    width: 45,
    height: 35,
    marginTop: 40,
    marginRight: 30,
    tintColor: 'white'
  },
  checkIcon: {
    flex: 4,
    flexDirection: 'row',
    alignItems: 'flex-end',
    justifyContent: 'center'
  },
  icon: {
    tintColor: 'white',
  },
  buttons: {
    flex: 4,
    justifyContent: 'flex-start',
    paddingTop: 30
  },
  saveButton: {
    width: '100%',
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#4E7E80'
  },
  saveText: {
    color: 'white',
    fontFamily: "AvenirNext-Regular",
    fontSize: 30
  }
});