from skfuzzy.control.visualization import FuzzyVariableVisualizer

"""
    skfuzzy kütüphanesini ile grafikleri çıktısını alırken aşağıdaki hatayı alıyorduk.

    Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.fig.show()

    Çözüm olarak kütüphanenin ilgi metodunu değiştirdik.

"""
def view(self, *args, **kwargs):
    """""" + FuzzyVariableVisualizer.view.__doc__
    fig, ax = FuzzyVariableVisualizer(self).view(*args, **kwargs)
    fig.savefig(f"app/static/graphic/{kwargs.get('name')}.png")