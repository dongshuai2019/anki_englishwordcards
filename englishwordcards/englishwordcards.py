from aqt import mw
from aqt.utils import showInfo
from aqt.qt import *
import anki
from PyQt5 import QtWidgets
from .tools import searchWord_renren,searchWord_kelin

def search_word(browser,type=0):
    # if type == 0:
    #     showInfo('科林辞典')
    # else:
    #     showInfo('人人词典')

    notes = [
        mw.col.getNote(note_id)
        for note_id in browser.selectedNotes()
    ]

    total = len(notes)
    n = 0
    for note in notes:
        result = ''
        if type == 0:
            result = searchWord_kelin(note['Front'])
        else:
            result = searchWord_renren(note['Front'])
        if result == '':
            # showInfo('查询失败，可以尝试使用别的词典')
            n += 1
        else:
            # showInfo('查询成功'+note['Back'])
            note['Back'] = result
            note.flush()
    mw.reset()
    msg = '查询单词'+str(total)+'个，其中'+str(total-n)+'个成功，'+str(n)+'个失败'
    showInfo(msg)

def on_setup_menus(browser):

    menu = QtWidgets.QMenu("单词宝", browser.form.menubar)
    browser.form.menubar.addMenu(menu)

    def kelin():
        search_word(browser,type=0)
    def renren():
        search_word(browser, type=1)

    action = menu.addAction("柯林辞典")
    action.triggered.connect(kelin)
    action = menu.addAction("人人辞典")
    action.triggered.connect(renren)


anki.hooks.addHook(
    'browser.setupMenus',
    on_setup_menus,
)