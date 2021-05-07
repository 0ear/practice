import  tensorflow as tf
import os
import  sys
import  warnings
stderr=sys.stderr
print('程式一開始執行建議不要載入nogpu.py')
sys.stderr=open(os.devnull,'w')
def nogpu():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
    # Windows常見的錯誤訊息進行排除
    print('以下為tensorflow 2.x 時代 Windows環境')
    tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)
    print('mac環境的Libaray設定')
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    print('處理tensorflow偵測numpy版本的錯誤訊息')
    print('以下語法會遮住所有警告訊息')
    warnings.filterwarnings('ignore')



