## hides the current active layer and then creates a copy of the visible layer
## afterwards create a group with the active layer and visible layer with a transparency mask

from krita import *
app = Krita.instance()
active = Krita.instance().activeDocument().activeNode()
doc = app.activeDocument()
root = doc.rootNode()

height = doc.height()
width = doc.width()
active.setVisible(False)
Krita.instance().activeDocument().refreshProjection()


root.removeChildNode(active)

copy_node = doc.pixelData(0,0,width,height)
new_copy = app.activeDocument().createNode('Visible','paintLayer')
Krita.instance().activeDocument().refreshProjection()

new_copy.setPixelData(copy_node,0,0,width,height)
Krita.instance().activeDocument().refreshProjection()

new_group = doc.createGroupLayer('PhotoBash'+active.name())
root.addChildNode(new_group,None)

new_group.addChildNode(new_copy,None)
new_group.addChildNode(active,new_copy)



erase = doc.createTransparencyMask ('erase visible')
active.addChildNode(erase,None)


active.setVisible(True)
new_copy.setLocked(True)
doc.setActiveNode(erase)
Krita.instance().activeDocument().refreshProjection()
