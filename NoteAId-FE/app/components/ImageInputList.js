import React, {useRef} from 'react';
import { View, StyleSheet, ScrollView } from 'react-native';
import colors from '../config/colors';
import ImageInput from './ImageInput';

function ImageInputList({imageUris = [], onRemoveImage, onAddImage, style, addLogo="camera", logoBackgroundColor="colors.photo"}) {
  const scrollView = useRef();
    return (
        <View>
        <ScrollView 
        ref={scrollView}
        vertical 
        persistentScrollbar={false}
        onContentSizeChange={() =>   scrollView.current.scrollToEnd()}
        >
      <View style={[styles.container, style]}>
        {imageUris.map(uri => 
        <View key={uri} style={styles.image}>
            <ImageInput 
            imageUri={uri} 
            onChangeImage={() => onRemoveImage(uri)}
            />
        </View>
        )}
        <ImageInput onChangeImage={uri => onAddImage(uri)}  style={[styles.add, {backgroundColor:logoBackgroundColor}]} logo={addLogo} logoColor={colors.white}/>
    </View>
    </ScrollView>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
      flexDirection: 'column',
  },
  image:{
      marginRight: 10,
  },
  add:{
    height: 60,
    width: 60,
    borderRadius: 30,
    marginBottom: 50,
    alignSelf: 'center',
    backgroundColor: colors.photo,
    borderColor: colors.white,
    borderWidth: 2,
  }
});

export default ImageInputList;