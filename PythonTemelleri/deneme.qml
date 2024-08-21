import QtQuick 6.0
import QtQuick.Controls 6.0

ApplicationWindow {
    visible: true
    width: 640
    height: 480
    title: "Hello, QML"

    Button {
        text: "Click me"
        anchors.centerIn: parent
        onClicked: {
            console.log("Button clicked!")
            pyButton.clicked()
        }
    }
}
