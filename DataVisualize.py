from matplotlib import pyplot as plt
from matplotlib import rc


class DataVisualize:
    def __init__(self, place, target, updateDate, total, overseas=None, local=None, non_symptom=None):
        self.total = total
        self.non_symptom = non_symptom
        self.overseas = overseas
        self.local = local
        self.updateDate = updateDate
        self.place = place
        # 判断省还是区
        self.target = target

        font = {
            'size': 18,
            'weight': 'light'
        }
        rc('font', **font)

    def create_figure(self):
        plt.figure(figsize=(20, 8), dpi=200, facecolor='#BDB76B')
        plt.title(f'{self.place}疫情动态走势', loc='left')
        plt.xlabel('日期', loc='right')
        plt.ylabel('确诊人数', loc='top')
        plt.xticks(range(0, len(self.updateDate), 6), self.updateDate[::6], rotation=15)

    def draw(self):

        if self.target == 'province':
            DataVisualize.create_figure(self)
            pattern_for_local = {
                'linestyle': '-.',
                'color': '#FFB6C1',
                'linewidth': 3.5,
                'label': '本地病例'
            }
            plt.plot(self.updateDate, self.local, **pattern_for_local)

            pattern_for_overseas = {
                'linestyle': '-.',
                'color': '#DDA0DD',
                'linewidth': 3.5,
                'label': '境外输入'
            }
            plt.plot(self.updateDate, self.overseas, **pattern_for_overseas)
            plt.legend()
            plt.grid(alpha=0.4)
            plt.savefig(f'{self.place}本地确诊与境外输入走势.png')
            plt.show()

        elif self.target == 'district':
            DataVisualize.create_figure(self)
            pattern_for_local = {
                'linestyle': '-.',
                'color': '#FFB6C1',
                'linewidth': 3.5,
                'label': '本地病例'
            }
            plt.plot(self.updateDate, self.local, **pattern_for_local)

            pattern_for_non_symptom = {
                'linestyle': '-.',
                'color': '#DDA0DD',
                'linewidth': 3.5,
                'label': '无症状感染者'
            }
            plt.plot(self.updateDate, self.non_symptom, **pattern_for_non_symptom)
            plt.legend()
            plt.grid(alpha=0.4)
            plt.savefig(f'{self.place}无症状感染者与确诊病例走势.png')
            plt.show()

        DataVisualize.create_figure(self)
        pattern_for_total = {
            'linestyle': '--',
            'color': '#FF8C00',
            'linewidth': 3.5,
            'label': '总确诊人数'
        }
        plt.plot(self.updateDate, self.total, **pattern_for_total)
        for x, y in zip(self.updateDate, self.total):
            if y > 0:
                plt.text(x, y, y, fontsize=13, ha="center", va="bottom", color='black')
        plt.legend()
        plt.grid(alpha=0.4)
        plt.savefig(f'{self.place}日新增确诊病例走势.png')
        plt.show()
