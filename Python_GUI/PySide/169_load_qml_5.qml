import QtQuick 1.0

Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"

    Rectangle {
        id: r1
        width: 100
        height: 100
        color: "gray"
        anchors.verticalCenter: main.verticalCenter
        Item {
           anchors.fill: parent
           focus: true
           Keys.onDigit1Pressed: parent.color = "red"
        }
        MouseArea {
            anchors.fill: parent
            onClicked: parent.color = "#ffff00"
        }
    }

    Rectangle {
        id: r2
        width: 100
        height: 100
        color: "gray"
        anchors.left: r1.right
        Item {
           anchors.fill: parent
           Keys.onDigit2Pressed: parent.color = "blue"
        }
        MouseArea {
            anchors.fill: parent
            onClicked: parent.color = "#00ffff"
        }
    }

    Rectangle {
        id: r3
        width: 100
        height: 100
        color: "gray"
        anchors.left: r2.right
        anchors.top: r2.bottom
        Item {
           anchors.fill: parent
           Keys.onDigit3Pressed: parent.color = "yellow"
        }
        MouseArea {
            anchors.fill: parent
            onClicked: parent.color = "#ff00ff"
        }
    }
}
