from krita import *
## for use with the cyanic krita plugin to quickly
## group indiviudal layers for photobashing

def extract_layer_from_group():
    app = Krita.instance()
    active = Krita.instance().activeDocument().activeNode()
    doc = app.activeDocument()
    root = doc.rootNode()

    height = doc.height()
    width = doc.width()


    groupNode = active.parentNode()

    if groupNode == root:
        QMessageBox.information(QWidget(), i18n("Python Custom Script Error"), i18n("active layer is not in a group"))
        return


    groupNode.setVisible(False)


    Krita.instance().activeDocument().refreshProjection()
    copy_node = doc.pixelData(0,0,width,height)
    new_copy = app.activeDocument().createNode('Visible','paintLayer')
    Krita.instance().activeDocument().refreshProjection()
    new_copy.setPixelData(copy_node,0,0,width,height)


    new_group = doc.createGroupLayer(active.name())
    root.addChildNode(new_group,None)

    erase_group = doc.createGroupLayer('erase')
    erase = doc.createNode('erase','paintLayer')
    erase.setBlendingMode('erase')
    erase_group.addChildNode(new_copy,None)
    erase_group.addChildNode(erase,None)


    groupNode.removeChildNode(active)
    new_group.addChildNode(active,None)
    new_group.addChildNode(erase_group,None)
    active.setVisible(True)
    Krita.instance().activeDocument().refreshProjection()
extract_layer_from_group()