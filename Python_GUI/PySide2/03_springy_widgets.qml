import QtQuick 2.0

Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"

    Rectangle {
        id: r1
        width: 64
        color: "red"
        opacity: 0.5
        anchors.left: parent.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
    }

    Rectangle {
        id: r2
        width: 160
        height: 160
        color: "yellow"
        opacity: 0.5
        z: 1
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }

    Rectangle {
        id: r3
        width: 64
        height: 160
        color: "blue"
        opacity: 0.5
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
    }
}
