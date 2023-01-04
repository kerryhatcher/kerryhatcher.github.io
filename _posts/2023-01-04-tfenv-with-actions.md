---
title: "Using TFENV with GitHub Actions"
date: 2022-01-04 01:00:00
description: Make use of tfenv's .terraform-version file when running terraform in GitHub Actions 
featured_image: '/images/better-python-logging/chris-ried-ieic5Tq8YMk-unsplash.jpg'
author: kerry
---



Wouldn't it be great if hashicorp/setup-terraform would automaticly make use of tfenv's .terraform file? 
Since it doesn't lets extract the contents of the file and pass that along to the setup-terraform action:


```
- name: Use terraform-version
      id: terraform-version
      shell: bash
      run: |
        TERRAFORM_VERSION="${{ github.workspace }}/.terraform-version"
        if [ -f "$TERRAFORM_VERSION" ]; then
            echo ".terraform-version file exists"
            echo "Setting terraform version defined in .terraform-version"
            echo ::set-output name=version::$(cat $TERRAFORM_VERSION)
        else
            echo ".terraform-version does not exist."
            echo "Using `latest` terraform version"
            echo ::set-output name=version::latest
        fi
```


---
Orginal credit goes to [Ezbon Jacob](https://github.com/codezninja) and [Jason Antman](https://github.com/jantman)   
---
   
Photo by [engin akyurt](https://unsplash.com/@enginakyurt?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/images/nature/cloud?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)
  
