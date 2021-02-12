import QtQuick 2.13
import QtQuick.Window 2.13
import QtQuick.Controls 2.15
import QtQuick.Controls.Material 2.0

Window {
    id:window
    width: 640
    height: 480
    visible: true
    color: "#4a0745"
    title: qsTr("Hello World")
    Button {
        id: button1
        x: 0
        y: 0
        text: qsTr("Кнопка 1")
        onClicked: {console.log("QML CLICK button 1"); backend.click_button1("button1") }
    }
    Button {
        id: button2
        x: 540
        y: 0
        text: qsTr("Кнопка 2")
        onClicked: {console.log("QML CLICK button 2"); backend.click_button2("button2")}
    }

    Label {
        id: label
        x: 307
        y: 188
        color: "#ffffff"
        text: qsTr("Label")
        horizontalAlignment: Text.AlignHCenter
        font.pointSize: 12
        styleColor: "#b82525"
        renderType: Text.NativeRendering
        clip: false
        Connections {
                target: backend // Указываем целевое соединение

                function onLableSignal(count){
                    label.text=count
                }
            }
    }

}

