import React, { useState } from "react";
import { View, StyleSheet, TouchableOpacity, Image, Text } from 'react-native';
import { MaterialCommunityIcons } from "@expo/vector-icons";
import * as Linking from 'expo-linking';
import RadioButtonRN from 'radio-buttons-react-native';

import colors from '../config/colors';
import Screen from '../components/Screen'
import AppText from '../components/Text';
import NAButton from '../components/NAButton';

function SavePhotoScreen({ route, text = "Summarizing", color = colors.photo, onPressView, onPressSave, nextScreen = "Confirm", navigation }) {
    onPressSave = () => navigation.navigate("Confirm");
    const { images } = route.params;

    const [summaryLevel, setSummaryLevel] = useState("");
    const [summaryLevelDisplay, setSummaryLevelDisplay] = useState("flex");
    const [loadingDisplay, setLoadingDisplay] = useState("none");
    const [viewFileDisplay, setViewFileDisplay] = useState("none");
    const [pageTitle, setPageTitle] = useState("Upload Files");

    const [pdfUrl, setPdfUrl] = useState("");

    const summaryLevelData = [
        {
            label: 'Short',
        },
        {
            label: 'Medium',
        },
        {
            label: 'Long'
        }
    ];

    const handleUpload = async () => {
        if (summaryLevel && summaryLevel != "") {
            setSummaryLevelDisplay("none");
            setLoadingDisplay("flex");

            await uploadImages();
            setLoadingDisplay("none");
            setViewFileDisplay("flex");
            setPageTitle("Done")
        }
    }

    const handleFileOpen = () => {
        Linking.openURL(pdfUrl);
    }

    const uploadImages = async () => {
        const host = "http://34.127.58.131";
        const formData = new FormData();

        let i = 1;
        for (const image of images) {
            const ext = image.split('.').slice(-1);
            formData.append('files[]', {
                name: `image${i}.${ext}`,
                type: 'image/' + ext,
                uri: Platform.OS === 'ios' ? image.replace('file://', '') : image,
            });
            i++;
        }

        await fetch(host + '/summarize_images?summ_level=' + summaryLevel.toLowerCase(), {
            method: 'POST',
            body: formData
        })
            .then((res) => res.json())
            .then((res) => {
                const fileURL = host + res.uri;
                setPdfUrl(fileURL);
                // console.log("Finished fetching: ", fileURL);
                // downloadPdf(host + fileURI);
            });
    }

    // const downloadPdf = async (url) => {
    //     FileSystem.downloadAsync(
    //         url,
    //         FileSystem.documentDirectory + 'testSummary.pdf'
    //     )
    //         .then(({ uri }) => {
    //             console.log('Finished downloading to ', uri);
    //             Linking.openURL(uri);
    //         })
    //         .catch(error => {
    //             console.error(error);
    //         });
    // };

    return (
        <View style={[styles.container, { backgroundColor: color }]}>
            <Screen style={{ width: "100%", alignItems: "center", marginTop: 30 }}>
                <View style={styles.topBar}>
                    <AppText style={styles.txt}>{pageTitle}</AppText>
                </View>
                <View style={{ display: summaryLevelDisplay }}>
                    <Text style={{ color: "#fff", marginBottom: 10, marginTop: 80, fontSize: 19, }}>Summary Length:</Text>
                    <RadioButtonRN
                        data={summaryLevelData}
                        selectedBtn={(e) => setSummaryLevel(e.label)}
                        boxDeactiveBgColor={"transparent"}
                        style={{ width: 300, }}
                        textStyle={{ color: "#fff" }}
                        activeColor={"#4ecdc4"}
                        initial={2}
                    />
                    <TouchableOpacity activeOpacity={0.8} onPress={handleUpload} style={{
                        height: 60,
                        alignItems: 'center',
                        justifyContent: 'center',
                        backgroundColor: "#4ecdc4",
                        borderRadius: 10,
                        marginTop: 50
                    }}>
                        <View style={{}}>
                            <Text style={{ color: "#fff", fontSize: 17 }}>Upload!</Text>
                        </View>
                    </TouchableOpacity>
                </View>

                <View style={{ display: loadingDisplay, alignItems: 'center', justifyContent: 'center', height: "40%", marginTop: 80 }}>
                    <Image style={{ height: 120, width: 120 }} source={require('../assets/infinity.gif')} />
                    <Text style={{ color: "#fff" }}>Loading...</Text>
                </View>

                <View style={{ height: "70%", alignItems: 'center', justifyContent: 'center', display: viewFileDisplay }}>
                    <Text style={{ color: "#fff", fontSize: 18 }}>Your summarized notes are ready!</Text>
                    <TouchableOpacity activeOpacity={0.8} onPress={handleFileOpen} style={{
                        height: 60,
                        alignItems: 'center',
                        justifyContent: 'center',
                        backgroundColor: "#4ecdc4",
                        borderRadius: 10,
                        marginTop: 40,
                        width: 300
                    }}>
                        <View style={{}}>
                            <Text style={{ color: "#fff", fontSize: 18 }}>View</Text>
                        </View>
                    </TouchableOpacity>
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
        justifyContent: 'center',
    },
    txt: {
        marginTop: 10,
        marginBottom: 20,
        color: colors.white,
        fontSize: 20,
        alignSelf: "center",
    },
    topBar: {
        flexDirection: "row",
        width: "100%",
        justifyContent: "center",
    },
    subText: {
        flex: 1,
        justifyContent: "center",
        alignItems: "center",
    },
    vsButton: {
        width: "40%",
        backgroundColor: "black",
        margin: 10,
    },
    rightArrow: {
        position: "absolute",
        right: 20,
    }
});

export default SavePhotoScreen;