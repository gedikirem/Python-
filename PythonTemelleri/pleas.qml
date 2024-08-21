import QtQuick 2.15
import QtQuick.Controls 2.15

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "My First QML App"

    Button {
        text: "Press Me"
        anchors.centerIn: parent
        onClicked: console.log("Button Pressed")
        background: Rectangle {
            color: "red" // Butonun arka plan rengini değiştirir
            radius: 5 // Köşeleri yuvarlatır
        }
    }
}
