import QtQuick 2.0

Rectangle {
    id: main
    width: 320
    height: 240
    color: "lightgray"

    property int animatedValue1: 50
    SequentialAnimation on animatedValue1 {
        loops: Animation.Infinite
        PropertyAnimation { to: 100; duration: 1000 }
        PropertyAnimation { to: 50; duration: 1000 }
    }

    property int animatedValue2: 50
    SequentialAnimation on animatedValue2 {
        loops: Animation.Infinite
        PropertyAnimation { to: 100; duration: 2000 }
        PropertyAnimation { to: 50; duration: 2000 }
    }

    property int animatedValue3: 50
    SequentialAnimation on animatedValue3 {
        loops: Animation.Infinite
        PropertyAnimation { to: 100; duration: 3000 }
        PropertyAnimation { to: 50; duration: 3000 }
    }

    property int animatedValue4: 0
    SequentialAnimation on animatedValue4 {
        loops: Animation.Infinite
        PropertyAnimation { to: 320; duration: 6000 }
        PropertyAnimation { to: 0; duration: 6000 }
    }

    Image {
        id: left_image
        source: "editors/vim.svg"
        width: parent.animatedValue1
        height: parent.animatedValue1
        anchors.verticalCenter: parent.verticalCenter
        anchors.left: parent.left
    }

    Image {
        id: center_image
        source: "editors/emacs.svg"
        width: parent.animatedValue2
        height: parent.animatedValue2
        anchors.horizontalCenter: parent.horizontalCenter
        anchors.verticalCenter: parent.verticalCenter
    }

    Image {
        id: right_image
        source: "editors/atom.svg"
        width: parent.animatedValue3
        height: parent.animatedValue3
        anchors.verticalCenter: parent.verticalCenter
        anchors.right: parent.right
    }

    Rectangle {
        id: r1
        width: parent.animatedValue4
        height: 30
        color: "red"
        opacity: 0.5
        anchors.left: parent.left
        anchors.top: parent.top
    }

}
