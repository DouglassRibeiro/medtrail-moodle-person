# static img

Quando você hardcodeia o caminho como /static/..., o Django não consegue gerenciar esse arquivo de forma dinâmica. Se você ativar o staticfiles em produção com hash no nome dos arquivos (ManifestStaticFilesStorage), o nome da imagem muda e o seu link quebra.

A melhor escolha, unindo o Tailwind CSS com o sistema de templates do Django, é injetar a tag {% static %} diretamente no estilo arbitrário do Tailwind. 

Porém já que não é possiivel fazer isso diretamente na class="" adicione a propriedade style="" e organize o {% static %} nela:

```html
<div class="-z-10 absolute inset-0 bg-cover bg-center bg-no-repeat blur-sm scale-105" 
     style="background-image: url('{% static 'core/img/Image_2ljwx32ljwx32ljw.webp' %}');">
</div>
```

há! .webp é mais leve.