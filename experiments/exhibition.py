from matplotlib import pyplot, patches
from numpy import load, median, min, max, log10


used_colors = [["#FE817D", "#FCBBAE"], ["#81B8DF", "#B1CCDF"]]
labels = ["customized", "numpy.sum"]

if __name__ == "__main__":
    bias = [-0.25, 0.25]
    data = load("result.2.npy")
    for data_index in range(4):
        for bias_index in range(2):
            used_data = data[data_index, bias_index]
            if min(used_data) > 1e-10:
                used_data = log10(used_data)
                if max(used_data) - min(used_data) < 0.02:
                    result = median(used_data)
                    pyplot.hlines(result, data_index + bias[bias_index] - 0.08, data_index + bias[bias_index] + 0.08,
                                  linewidths=1, edgecolors=used_colors[bias_index][0], zorder=3)
                    pyplot.scatter([data_index + bias[bias_index]], result,
                                   color="white", edgecolor=used_colors[bias_index][0], linewidth=1, s=20, zorder=4)
                else:
                    violin = pyplot.violinplot(dataset=used_data, positions=[data_index + bias[bias_index]],
                                               bw_method=0.5, showextrema=False, widths=0.3)
                    for patch in violin["bodies"]:
                        patch.set_edgecolor(used_colors[bias_index][0])
                        patch.set_facecolor(used_colors[bias_index][1])
                        patch.set_linewidth(1)
                        patch.set_alpha(1)
                    pyplot.scatter([data_index + bias[bias_index]], median(used_data),
                                   color="white", edgecolor=used_colors[bias_index][0], linewidth=1, s=40, zorder=4)
            else:
                pyplot.scatter([data_index + bias[bias_index]], [-2],
                               color=used_colors[bias_index][0], marker="x", s=60)

        if data_index % 2 != 0:
            pyplot.fill_between([data_index - 0.5, data_index + 0.5], [-2.2, -2.2], [3.2, 3.2],
                                color="#F1F1F1", zorder=0)

    legends = [patches.Patch(facecolor=used_colors[index][1], edgecolor=used_colors[index][0],
                             linewidth=1, label=labels[index]) for index in range(2)]
    pyplot.legend(handles=legends, loc="upper left", fontsize=12)

    pyplot.xlabel("different number of samples with 20 variables", fontsize=12)
    pyplot.xlim(-0.5, 3.5)
    pyplot.xticks([0, 1, 2, 3], [r"$500$", r"$1000$", r"$5000$", r"$10000$"], fontsize=12)
    pyplot.ylabel("seconds spent", fontsize=12)
    pyplot.ylim(-2.2, 3.2)
    pyplot.yticks([-2, -1, 0, 1, 2, 3],
                  ["$10^{-2}$", "$10^{-1}$", "$10^0$", "$10^1$", "$10^2$", "$10^3$"], fontsize=12)

    pyplot.savefig("result.2.svg", format="svg", bbox_inches="tight", dpi=600)
    pyplot.close()

    # pyplot.figure(figsize=(10, 5), tight_layout=True)
    # bias = [-0.3, 0, 0.3]
    # data = load("result.2.npy")
    # for data_index in range(3):
    #     for bias_index in range(3):
    #         used_data = data[data_index, bias_index]
    #         if min(used_data) > 1e-10:
    #             used_data = log10(used_data)
    #             if max(used_data) - min(used_data) < 0.02:
    #                 result = median(used_data)
    #                 pyplot.hlines(result, data_index + bias[bias_index] - 0.08, data_index + bias[bias_index] + 0.08,
    #                               linewidths=1, edgecolors=used_colors[bias_index][0], zorder=3)
    #                 pyplot.scatter([data_index + bias[bias_index]], result,
    #                                color="white", edgecolor=used_colors[bias_index][0], linewidth=1, s=20, zorder=4)
    #             else:
    #                 violin = pyplot.violinplot(dataset=used_data, positions=[data_index + bias[bias_index]],
    #                                            bw_method=0.5, showextrema=False, widths=0.16)
    #                 for patch in violin["bodies"]:
    #                     patch.set_edgecolor(used_colors[bias_index][0])
    #                     patch.set_facecolor(used_colors[bias_index][1])
    #                     patch.set_linewidth(1)
    #                     patch.set_alpha(1)
    #                 pyplot.scatter([data_index + bias[bias_index]], median(used_data),
    #                                color="white", edgecolor=used_colors[bias_index][0], linewidth=1, s=20, zorder=4)
    #         else:
    #             pyplot.scatter([data_index + bias[bias_index]], [-2],
    #                            color=used_colors[bias_index][0], marker="x", s=30)
    #
    #     if data_index % 2 != 0:
    #         pyplot.fill_between([data_index - 0.5, data_index + 0.5], [-2.2, -2.2], [3.2, 3.2],
    #                             color="#F1F1F1", zorder=0)
    #
    # legends = [patches.Patch(facecolor=used_colors[index][1], edgecolor=used_colors[index][0],
    #                          linewidth=1, label=labels[index]) for index in range(3)]
    # pyplot.legend(handles=legends, loc="upper left", fontsize=12)
    #
    # pyplot.xlabel("different number of samples with 100 variables", fontsize=12)
    # pyplot.xlim(-0.5, 3.5)
    # pyplot.xticks([0, 1, 2, 3], ["$10^1$", "$10^2$", "$10^3$", "$10^4$"], fontsize=12)
    # pyplot.ylabel("average seconds spent", fontsize=12)
    # pyplot.show()
    # # pyplot.ylim(-2.2, 3.2)
    # # pyplot.yticks([-2, -1, 0, 1, 2, 3], ["10^{-2}", "10^{-1}", "10^0", "10^1", "10^2", "10^3"], fontsize=12)