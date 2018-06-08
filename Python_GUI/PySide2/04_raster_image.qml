import QtQuick 2.0

Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"

    Rectangle {
        id: left_rectangle
        color: "red"
        opacity: 0.5
        anchors.left: parent.left
        anchors.right: image.left
        anchors.top: parent.top
        anchors.bottom: parent.bottom
    }

    Image {
        id: image
        source: "images/voronoi.png"
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }

    Rectangle {
        id: right_rectangle
        color: "blue"
        opacity: 0.5
        anchors.left: image.right
        anchors.right: parent.right
        anchors.top: parent.top
        anchors.bottom: parent.bottom
    }
}
