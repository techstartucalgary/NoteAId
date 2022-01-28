import React from 'react';
import { View, Text, StyleSheet, Image } from 'react-native';

const App = () => {
  return (
    <View style={styles.container}>
      <Image source={require('./assets/bkgBlack.png')} style={styles.backgroundImage}/>
      <View style={styles.footer}>
        <Text style={styles.title}>Processing Photo</Text>
        <View style = {styles.icon}>
          <Image source={require('./assets/loading.png')} style={styles.loadingIcon}/>
        </View>
        <View style = {styles.content}>
          <Text style={styles.descriptionText}>Sit tight, our AI is working hard</Text>
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
  title: {
    fontFamily: 'AvenirNext-UltraLight',
    fontSize: 35,
    marginTop: 30,
    color: 'white'
  },
  icon: {
    flex: 6,
    flexDirection: 'row',
    alignItems: 'flex-end',
    justifyContent: 'center'
  },
  loadingIcon: {
    tintColor: 'white',
    width: 150,
    height: 150
  },
  content: {
    flex: 5,
    flexDirection: 'row',
    alignItems: 'flex-start',
    justifyContent: 'center',
    paddingHorizontal: 40,
    paddingTop: 40
  },
  descriptionText: {
    fontFamily:'AvenirNext-UltraLight',
    fontSize: 20,
    color: 'white',
    textAlign: 'center'
  }
});

